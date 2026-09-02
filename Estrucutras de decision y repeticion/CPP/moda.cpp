#include <iostream>
#include <cstdlib>

using namespace std;

void imprimirVec(int vec[], int n)
{
    int i; 
    for (i = 0; i < n; i++)
    {
        cout << vec[i] << " ";
    }
}

int revisarSubVec(int vec[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (x == vec[i]) 
        {
            return 0;
        }
    }
    return 1;
} // devuelve 0 si el numero aparece en el vector, 1 si no aparece.

int main()
{
    int i, j, t, n;
    cout << "Introduzca el número de elementos del vector: ";
    cin >> n;
    int A[n];
    int R[n];
    srand(time(0));
    for (i = 0; i < n; i++)
    {
        A[i] = rand() % 10;
    }
    cout << "Vector original: \n"; 
    imprimirVec(A, n);
    cout << endl;
    // moda, multimodal
    // primero, hallar un vector con los elementos únicos. Y contar cuantos instancias de cada número hay.
    // no se si sea el mejor algoritmo, pero vamos a ver.
    for (i = 0; i < n; i++)
    {
        // el primer ciclo, recorre todos lo elementos para buscar repeticiones
        int cont = 0;
        for (j = 0; j < n; j++)
        {
            if (A[i] == A[j])
            {
                cont++;
            }
        }
        R[i] = cont;
    }
    imprimirVec(A, n);
    cout << endl;
    cout << "conteo por elemento: " << endl;
    imprimirVec(R, n);
    cout << endl;
    // tengo las apariciones de cada elemento, ahora debo hallar el máximo, eso daría una sola moda.
    int max = R[0], maxIndice = 0;
    for (i = 1; i < n; i++)
    {
        if (R[i] > max)
        {
            max = R[i];
            maxIndice = i;
        }
    } 
    cout << "el máximo inicial es " << A[maxIndice] << " con " << max << " apariciones" << endl;
    // ahora, debemos revisar cuantas veces aparece ese máximo, y mirar si hay valores diferentes, usando los dos vectores en paralelo.
    int m = 1; // se guardará acá el número total de máximos, o más bien, de máximos que correspondan 
                // a elementos distintos en el vector A
    int modas_aux[n]; // donde se guardarán temporalmente las modas.
    modas_aux[0] = A[maxIndice];
    for (i = 0; i < n; i++)
    {
        if (R[i] == max)
        {
            for ( j = 0; j < n; j++ )
            {
                if ( R[i] == R[j] && j != i )
                {
                    if (A[i] != A[j] && revisarSubVec(modas_aux, m, A[j]))
                    {
                        modas_aux[m] = A[j];
                        m++;
                    }
                }
            }
        }
    }
    cout << endl;
    cout << "Las modas son: " << endl;
    imprimirVec(modas_aux, m);
    cout << endl;
}