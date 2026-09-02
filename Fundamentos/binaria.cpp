#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int BusquedaBinaria(int *, int, int);

void imprimirVec(int vec[], int n)
{
    int i; 
    for (i = 0; i < n; i++)
    {
        cout << vec[i] << " ";
    }
}

int BusquedaBinaria(int *A, int N, int T)
{
    int L = 0, R = N - 1, m;
    while (L <= R)
    {
        m = floor((L + R) / 2);
        if (A[m] < T)
        {
            L = m + 1;
        } 
        else
            if (A[m] > T)
            {
                R = m - 1;    
            }
            else
            {
                return m;
            }
    }
    return -1;
}

int main(int argc, char *argv[])
{
    int n, t;
    srand(time(NULL));
    if (argc > 1)
    {
        n = stoi(argv[1]);
        t = stoi(argv[2]);    
    }
    else
    {
        n = 100;
        t = 50;
    }
    if (n <= 1)
        n = 100;
    int A[n];
    // llenado del vector
    for (int i = 0; i < n; i++)
    {
        A[i] = rand() % 100;
    }
    cout << "Vector generado" << endl;
    imprimirVec(A, n);
    // ordenamiento previo
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i -1; j++)
        {
            if (A[j] > A[j + 1])
            {
                swap(A[j], A[j + 1]);
            }
        }
    }
    cout << endl;
    cout << "Vector ordenado" << endl;
    imprimirVec(A, n);
    cout << endl;
    cout << "Buscar valor " << t << " en el vector ordenado" << endl;
    // int pos = BusquedaBinaria(A, n, t);
    int pos = -1;
    int L = 0, R = n - 1, m;
    while (L <= R)
    {
        m = floor((L + R) / 2);
        if (A[m] < t)
        {
            L = m + 1;
        } 
        else
            if (A[m] > t)
            {
                R = m - 1;    
            }
            else
            {
                pos = m;
                break;
            }
    }
    if (pos >= 0)
    {
        cout << "Posición del valor en el vector: " << pos << endl;
    }
    else
    {
        cout << "No se encontró en el vector" << endl;
    }
    

}