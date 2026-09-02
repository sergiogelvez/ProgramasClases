from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Style

print("Programa que genera un menú y solo permite continuar si se escoge una opción correcta.")

valida = False

while not valida:
    # nota, el 0 no se usa en este caso para evitar los casos en que se introduce algo que no es un número
    print("Menú de opciones -  Escoja un color")
    print("-1. Blanco")
    print("1. Rojo")
    print("2. Magenta")
    print("3. Amarillo")
    print("4. Verde")
    print("5. Azul")
    print("6. Cyan")
    print("7. Negro")
    print("0. Salir")
    # código para inicializar los colores
    just_fix_windows_console()
    #
    color = Fore.WHITE
    entrada = input("Introduzca un número correspondiente a una opción: ")
    opcion = entrada
    #opcion = int(entrada)
    match entrada:
        case '0':
            print(f"Su entrada fue {entrada}, Que corresponde a salir - ultimo color")
            valida = True
        case '-1':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Blanco")
            color = Fore.WHITE
            #valida = True
        case '1':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Rojo")
            color = Fore.RED
            #valida = True
        case '2':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Magenta")
            color = Fore.MAGENTA
            #valida = True
        case '3':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Amarillo")
            color = Fore.YELLOW
            #valida = True
        case '4':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Verde")
            color = Fore.GREEN
            #valida = True
        case '5':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Azul")
            color = Fore.BLUE
            #valida = True
        case '6':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Cyan")
            color = Fore.CYAN
            #valida = True
        case '7':
            print(f"Su entrada fue {entrada}, que corresponde a la opción {opcion} - Negro")
            color = Fore.BLACK
            #valida = True
        case other:
            print(f"Su entrada fue {entrada}, que no corresponde a ninguna opción - No es válida")
            valida = False
        
    # Ya se escogió el color, ahora se imprime el mensaje
    if opcion != '0':
        print(color + "Este fue el color escogido.")





    