#!/usr/bin/env python3
"""
tcpspy.py - Proxy TCP con registro de bytes.

Se interpone entre un cliente y un servidor y registra todo lo que pasa
por la conexion, en ambos sentidos, con marca de tiempo y volcado hexadecimal.

    cliente ---> tcpspy (127.0.0.1:9999) ---> servidor (127.0.0.1:8080)

Solo usa la biblioteca estandar: no requiere instalacion ni privilegios.

Uso basico
----------
    python tcpspy.py --escuchar 9999 --destino 127.0.0.1:8080

Luego el cliente se conecta al 9999 en vez del 8080.

Opciones didacticas
-------------------
    --trocear 4      reenvia los datos en trozos de 4 bytes (demuestra que TCP
                     es un flujo de bytes y no un flujo de mensajes)
    --retardo 250    inyecta 250 ms de latencia en cada reenvio
    --cortar 100     cierra la conexion tras reenviar 100 bytes en un sentido
    --archivo t.log  ademas de la consola, escribe el registro a un archivo

Escrito para el curso de Sistemas Distribuidos, UIS.
"""

import argparse
import socket
import sys
import threading
import time

# La consola de Windows suele venir en cp1252 y revienta con caracteres raros.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_candado = threading.Lock()
_salida = None
_contador_conexiones = 0


def registrar(texto):
    """Escribe en consola (y en archivo, si se pidio) de forma atomica."""
    with _candado:
        print(texto, flush=True)
        if _salida:
            _salida.write(texto + "\n")
            _salida.flush()


def volcado_hex(datos, limite, sangria=" " * 22):
    """Devuelve el volcado hexadecimal de `datos`, en lineas de 16 bytes."""
    lineas = []
    visibles = datos if limite == 0 else datos[:limite]
    for pos in range(0, len(visibles), 16):
        trozo = visibles[pos:pos + 16]
        hexa = " ".join(f"{b:02x}" for b in trozo)
        hexa = f"{hexa:<47}"  # 16 bytes * 3 - 1
        texto = "".join(chr(b) if 32 <= b < 127 else "." for b in trozo)
        lineas.append(f"{sangria}{hexa}  |{texto}|")
    if limite and len(datos) > limite:
        lineas.append(f"{sangria}... {len(datos) - limite} bytes mas")
    return "\n".join(lineas)


def bombear(origen, destino, etiqueta, id_conexion, t0, cfg):
    """Copia bytes de `origen` a `destino` registrando cada lectura."""
    total = 0
    lecturas = 0
    try:
        while True:
            datos = origen.recv(65536)
            if not datos:
                break

            lecturas += 1
            total += len(datos)
            t = time.monotonic() - t0
            registrar(f"[{t:8.4f}] #{id_conexion} {etiqueta} "
                      f"lectura {lecturas}: {len(datos)} bytes "
                      f"(acumulado {total})")
            if not cfg.silencioso:
                registrar(volcado_hex(datos, cfg.max_volcado))

            # Reenvio, posiblemente troceado y/o retardado.
            paso = cfg.trocear if cfg.trocear else len(datos)
            for pos in range(0, len(datos), paso):
                if cfg.retardo:
                    time.sleep(cfg.retardo / 1000.0)
                destino.sendall(datos[pos:pos + paso])

            if cfg.cortar and total >= cfg.cortar:
                t = time.monotonic() - t0
                registrar(f"[{t:8.4f}] #{id_conexion} {etiqueta} "
                          f"*** corte forzado tras {total} bytes ***")
                origen.close()
                destino.close()
                return
    except OSError as err:
        registrar(f"[{time.monotonic() - t0:8.4f}] #{id_conexion} {etiqueta} "
                  f"error de socket: {err}")
    finally:
        t = time.monotonic() - t0
        registrar(f"[{t:8.4f}] #{id_conexion} {etiqueta} FIN "
                  f"({total} bytes en {lecturas} lecturas)")
        # Cierre a medias: avisamos al otro extremo sin matar la conexion.
        try:
            destino.shutdown(socket.SHUT_WR)
        except OSError:
            pass


def atender(cliente, direccion, cfg):
    global _contador_conexiones
    with _candado:
        _contador_conexiones += 1
        id_conexion = _contador_conexiones

    t0 = time.monotonic()
    registrar(f"\n[{0.0:8.4f}] #{id_conexion} conexion nueva desde "
              f"{direccion[0]}:{direccion[1]}")

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.connect((cfg.host_destino, cfg.puerto_destino))
    except OSError as err:
        registrar(f"[{time.monotonic() - t0:8.4f}] #{id_conexion} "
                  f"no se pudo conectar al servidor: {err}")
        cliente.close()
        return

    hilos = [
        threading.Thread(target=bombear,
                         args=(cliente, servidor, "C->S", id_conexion, t0, cfg),
                         daemon=True),
        threading.Thread(target=bombear,
                         args=(servidor, cliente, "S->C", id_conexion, t0, cfg),
                         daemon=True),
    ]
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()

    cliente.close()
    servidor.close()
    registrar(f"[{time.monotonic() - t0:8.4f}] #{id_conexion} conexion cerrada")


def main():
    p = argparse.ArgumentParser(
        description="Proxy TCP que registra el trafico de una conexion.")
    p.add_argument("--escuchar", type=int, default=9999,
                   help="puerto local donde escucha el proxy (def. 9999)")
    p.add_argument("--destino", default="127.0.0.1:8080",
                   help="host:puerto del servidor real (def. 127.0.0.1:8080)")
    p.add_argument("--interfaz", default="127.0.0.1",
                   help="direccion local de escucha; deje 127.0.0.1 para "
                        "evitar el aviso del cortafuegos de Windows")
    p.add_argument("--trocear", type=int, default=0, metavar="N",
                   help="reenviar en trozos de N bytes")
    p.add_argument("--retardo", type=int, default=0, metavar="MS",
                   help="latencia artificial en milisegundos por reenvio")
    p.add_argument("--cortar", type=int, default=0, metavar="N",
                   help="cortar la conexion tras N bytes en un sentido")
    p.add_argument("--max-volcado", type=int, default=64, metavar="N",
                   help="bytes a mostrar en hexadecimal, 0 = todos (def. 64)")
    p.add_argument("--silencioso", action="store_true",
                   help="registrar solo tamanos, sin volcado hexadecimal")
    p.add_argument("--archivo", metavar="RUTA",
                   help="copiar el registro a un archivo de texto")
    cfg = p.parse_args()

    if ":" not in cfg.destino:
        p.error("--destino debe tener la forma host:puerto")
    cfg.host_destino, puerto = cfg.destino.rsplit(":", 1)
    cfg.puerto_destino = int(puerto)

    global _salida
    if cfg.archivo:
        _salida = open(cfg.archivo, "w", encoding="utf-8")

    escucha = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    escucha.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    escucha.bind((cfg.interfaz, cfg.escuchar))
    escucha.listen(16)

    registrar(f"tcpspy escuchando en {cfg.interfaz}:{cfg.escuchar} "
              f"-> {cfg.host_destino}:{cfg.puerto_destino}")
    registrar("Ctrl+C para terminar.\n")

    try:
        while True:
            cliente, direccion = escucha.accept()
            threading.Thread(target=atender,
                             args=(cliente, direccion, cfg),
                             daemon=True).start()
    except KeyboardInterrupt:
        registrar("\nterminado por el usuario")
    finally:
        escucha.close()
        if _salida:
            _salida.close()


if __name__ == "__main__":
    main()
