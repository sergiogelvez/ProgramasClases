#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *b;
    a = 100;
    b = &a;
    int c[] = {5, 1, 4, 7, 3};
    printf("valor de a: %d\n", a);
    printf("valor de dirección de a: %p\n", &a);
    printf("valor de b: %p\n", b);
    printf("valor de lo que b apunta: %d\n", *b);
    printf("valor de c: %d\n", *c);
    printf("valor de c + 1: %d\n", *(c + 1));
    printf("valor de c[0] + 1: %d\n", (*c) + 1);
    a = 120;
    printf("valor de a: %d\n", a);
    printf("valor de dirección de a: %p\n", &a);
    printf("valor de b: %p\n", b);
    printf("valor de lo que b apunta: %d\n", *b);
    printf("Se reincian a y b \n");
    b = (int *)malloc(sizeof(int));
    *b = 500;
    a = 120;
    printf("valor de a: %d\n", a);
    printf("valor de dirección de a: %p\n", &a);
    printf("valor de b: %p\n", b);
    printf("valor de lo que b apunta: %d\n", *b);
}