#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int *ordInsercionSimple(int [], int );
void ordInsercionAlt(int [], int );
int *ordBurbujaTrad(int [], int );
int *ordBurbujaAlt(int [], int );


void imprimirVec(int vec[], int n)
{
    int i; 
    for (i = 0; i < n; i++)
    {
        cout << vec[i] << " ";
    }
}

int main()
{
    int i, j, t, n;
    cout << "Introduzca el número de elementos del vector: ";
    cin >> n;
    int A[n];
    srand(time(0));
    for (i = 0; i < n; i++)
    {
        A[i] = rand() % 100;
    }
    cout << "Vector original: \n"; 
    imprimirVec(A, n);
    cout << endl;
    // algoritmo de ordenamiento por inserción, versión con intercambios
    /* i = 1;
    while (i < n)
    {
        j = i;
        while (j > 0 && (A[j - 1] > A[j]) )
        {
            cout << "(" << A[i] << ") : ";
            swap(A[j], A[j - 1]);
            j = j - 1;
            imprimirVec(A, n);
            cout << endl;
        }
        cout << "(" << A[i] << ") : ";
        imprimirVec(A, n);
        cout << endl;
        i = i + 1;
    } */
    //int *vec = ordInsercionSimple(A, n);
    // hacer el menu acá, ya tengo las cuatro funciones, incluso la que no sirve.
    int continuar = 1;
    int opc;
    while (continuar == 1)
    {
        cout << "\n\n" << "Menu" << '\n';
        cout << "1. Ordenar por burbuja tradicional\n";
        cout << "2. Ordenar por burbuja alternativo\n";
        cout << "3. Ordenar por inserción tradicional\n";
        cout << "4. Ordenar por inserción alternativo\n";
        cout << "5. Salir\n";
        cout << "Escoja una opción: ";
        cin >> opc;
        switch(opc)
        {
            case 1: {
                continuar = 1;
                break;
            }
            case 2: {
                int *vec = ordBurbujaAlt(A, n);
                //ordInsercionAlt(A, n);
                cout << "Vector original: \n";
                imprimirVec(A, n);
                cout << endl;
                cout << "Vector ordenado: \n";
                imprimirVec(vec, n);
                cout << endl;
                continuar = 1;
                break;
            }
            case 3: {
                continuar = 1;
                break;
            }
            case 4: {
                
                continuar = 1;
                break;
            }
            case 5: {
                cout << "Hasta pronto" << "\n\n" << endl;
                continuar = 0;
                break;
            }
        }
        
    }
    
}

int *ordInsercionSimple(int vec[], int n)
{
    int i, j;
    i = 1;
    while (i < n)
    {
        j = i;
        while ( j > 0 && (vec[j - 1] > vec[j]) )
        {
            swap(vec[j], vec[j - 1]);
            j = j - 1;
        }
        i = i + 1;
    }
    return vec;
}

void ordInsercionAlt(int vec[], int n)
{
    int i, j, t;
    i = 1;
    while (i < n)
    {
        t = vec[i];
        j = i - 1;
        while (j >= 0 && vec[j] > t)
        {
            vec[j + 1] = vec[j];
            j = j - 1;
        }
        vec[j + 1] = t;
        i = i + 1;
    }
}

int *ordBurbujaTrad(int vec[], int n)
{
    int *lista;
    lista = (int *)malloc(n*sizeof(int));
    for (int i = 0; i < n; i++) 
    {
        lista[i] = vec[i];
    }
    for (int i=0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (lista[j] > lista[j+1])
            {
                // temp = lista[j];
                // lista[j] = lista[j + 1];
                // lista[j + 1] = temp;
                swap(lista[j], lista[j + 1]);
            }
        }
    }
    return lista;
}

int *ordBurbujaAlt(int vec[], int n)
{
    int temp, lista[n];
    for (int i = 0; i < n; i++)
    {
        lista[i] = vec[i];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (lista[i] > lista[j])
            {
                temp = lista[j];
                lista[j] = lista[i];
                lista[i] = temp;
            }
        }
    }
    return lista;
}