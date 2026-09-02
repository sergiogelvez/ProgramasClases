#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <time.h>

int main()
{
    int n, i;
    std::cout << "Introduzca el número de elementos, por favor: ";
    std::cin >> n;
    srand(time(0));
    int elementos[n];
    // generación de los n elementos, con valores enteros entre 1 y 100
    for ( i = 0; i < n; i++ )
    {
        elementos[i] = 1 + rand() % 100;
    }

    // impresión en pantalla de los elementos generados.
    for ( i = 0; i < n; i++ )
    {
        printf("%d ", elementos[i]);
    }
    printf("\n");

    printf("Fin del programa\n");
}
