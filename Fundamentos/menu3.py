from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Style

print("Programa que genera un menú y solo permite continuar si se escoge una opción correcta.")

continuar = True

dicc_color = {
    "-1": ("Blanco", Fore.WHITE),
    "1": ("Rojo", Fore.RED),
    "2": ("Magenta", Fore.MAGENTA),
    "3": ("Amarillo", Fore.YELLOW),
    "4": ("Verde", Fore.GREEN),
    "5": ("Azul", Fore.BLUE),
    "6": ("Cyan", Fore.CYAN),
    "7": ("Negro", Fore.BLACK),
    "0": ("Salir", "")
}

color = Fore.WHITE

while continuar:
    # nota, el 0 no se usa en este caso para evitar los casos en que se introduce algo que no es un número
    print("Menú de opciones -  Escoja un color")
    for color in dicc_color.items():
        print(f"{color[0]}. {color[1][0]}")
    # código para inicializar los colores
    just_fix_windows_console()
    #
    
    entrada = input("Introduzca un número correspondiente a una opción: ")
    #opcion = int(entrada)
    if entrada in dicc_color.keys() :
        valor_color = dicc_color[entrada]
        nombre_color = valor_color[0]
        codigo_color = valor_color[1]
        #print(nombre_color, codigo_color)
        if (entrada == '0'):
            print(f"Su entrada fue {entrada}, Que corresponde a salir - ultimo color")
            continuar = False
        else:
            print(f"Su entrada fue {entrada}, que corresponde al color {nombre_color}")
            color = codigo_color
            # Ya se escogió el color, ahora se imprime el mensaje, en el mismo if
            print(color + "Este fue el color escogido.")
            continuar = True
        # 
    else:
        print(f"Su entrada fue {entrada}, que no corresponde a ninguna opción - No es válida")
        continuar = True
            
        
print("Fin del programa, todo está super")

        





    