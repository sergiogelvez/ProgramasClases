#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct registro
{
    char id[100];
    char nombres[100];
    char apellidos[100];
    int salarioBase;
    int horasExtra;
    int valorHoraBase;
}reg;

int main()
{
    reg listado[100]; // se asume un máximo de 100 líneas para el archivo, si se quiere dinámico, es necesario usar punteros.
    char nombre[] = "nomina1.txt";
    char* linea = NULL;
    char* token = NULL;
    size_t largoLinea = 0;
    FILE *archivo;
    archivo = fopen(nombre, "r");
    int contLineas = 0;
    ssize_t read;

    if (archivo == NULL)
    {
        printf("Archivo inválido.\n");
    }
    else
    {
        while (read = getline( &linea, &largoLinea, archivo) != -1)
        {
            // acá se separa en líneas
            printf("linea N %d: %s \n", contLineas, linea);
            int contTokens = 0;
            while ((token = strtok_r(linea, ";", &linea)))
            {
                // listado[contLineas].id = NULL;
                printf("%s", token);
                if (contTokens == 0) { strcpy(listado[contLineas].id, token); }
                if (contTokens == 1) { strcpy(listado[contLineas].apellidos, token); }
                if (contTokens == 2) { strcpy(listado[contLineas].nombres, token); }
                if (contTokens == 3) 
                {
                    listado[contLineas].salarioBase = atoi(token);
                    listado[contLineas].valorHoraBase = listado[contLineas].salarioBase / (30 * 8); 
                }
                if (contTokens == 4) { listado[contTokens].horasExtra = atoi(token); }
                contTokens++;
            }
            contLineas++;
            printf("Ultimo antes de procesar %d lineas...\n", contLineas);
        }
        printf("Procesando %d lineas...\n", contLineas);
        // fclose(archivo);
        // Acá se hace el proceso de las líneas
        FILE* salida;
        salida = fopen("salidac.csv", "w");
        char nCompleto[200];
        printf("Antes de entrar al for de solo imprimir el listado\n");
        for (int i = 0; i < contLineas; i++)
        {
            printf("Registro %d: %s %s %s %d %d %d\n", i, listado[i].id, listado[i].nombres, listado[i].apellidos, listado[i].salarioBase, listado[i].horasExtra, listado[i].valorHoraBase);
        }
        for (int i = 0; i < contLineas; i++)
        {
            printf("registro %d\n", i);
            fprintf(salida, "Registro %d: %s;%s %s;%d;%d;%d\n", i, listado[i].id, listado[i].nombres, listado[i].apellidos, listado[i].salarioBase, listado[i].horasExtra, listado[i].valorHoraBase);
            // fprintf(salida, "%s;%s;%d\n", listado[i].id, nCompleto, listado[i].valorHoraBase);
            
        }
        printf("Saliendo del for del archivo...\n");
        fclose(salida);
        printf("Se cerró el archivo de salida...\n");
        
    }
    return 0;
}