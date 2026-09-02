
#include <stdio.h>
#include <string.h>
 
int main()
{
    char str[100], str2[100], palabra1[20], palabra2[20];
    char* token;
    char* rest = str;
    printf("Introduzca la frase: ");
    fgets(str, 100, stdin);
    printf("Introduzca la palabra a buscar: ");
    scanf("%s", palabra1);
    printf("Introduzca la palabra a reemplazar: ");
    scanf("%s", palabra2);
    strcpy(str2,"");
    while ((token = strtok_r(rest, " ", &rest)))
    {
        printf("%s\n", token);
        // strcat(str2, token);
        if (strcmp(token, palabra1)!=0)
        {
            strcat(str2, token);
        }
        else
        {
            strcat(str2, palabra2);
        }
        strcat(str2, " ");
    }
    printf("La nueva frase es:\n");
    printf("%s", str2);
    return (0);
}

// El gato vuela por el bosque como el gato montez vuela por los cielos