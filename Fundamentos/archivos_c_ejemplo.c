#include <stdio.h>
#include <stdlib.h>

void imprimirVec(float vec[], int n)
{
    int i; 
    for (i = 0; i < n; i++)
    {
        printf("%f ", vec[i]);
    }
    printf("\n");
}

int main()
{
    int n, i;
    FILE *archivo;
    // char path[100] = "./Programas\ Clase\ 2022-[1\ 2]/Fundamentos/estaturas.txt";
    char path[100] = "estaturas.txt";
    archivo = fopen(path, "r");
    if (archivo == NULL)
    {
        printf("El archivo %s no existe\n ", path);
    }
    else
    {
        fscanf(archivo, "%d", &n);
        printf("Leyendo %d lineas:\n", n);
        float estaturas[n], pesos[n];
        for (i = 0; i < n; i++)
        {
            fscanf(archivo, "%f %f", &estaturas[i], &pesos[i]);
        }
        imprimirVec(estaturas, n);
        imprimirVec(pesos, n);
    }
    
}