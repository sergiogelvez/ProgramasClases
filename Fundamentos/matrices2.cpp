#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

void imprimirMatriz( int v[], int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << v[i*m+j] << " ";
        }
        cout << '\n';
    }
}

int main()
{
    int n, m, p;
    cout << "Introduzca los valor de n, m, p " << '\n';
    cin >> n;
    cin >> m;
    cin >> p;
    float A[n*m], B[m*p], C[n*p];
    srand(time(0));
    int i, j;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            A[i*m + j] = rand() % 5;            
        }
    }
    // matriz B
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < p; j++)
        {
            B[i * p + j] = rand() % 5;            
        }
    }
    // imprimirMatriz(n, m, A);
    cout << "Matriz A:" << '\n';
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << A[i * m + j] << " ";
        }
        cout << '\n';
    }
    cout << "Matriz B:" << '\n';
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++)
        {
            cout << B[i * p + j] << " ";
        }
        cout << '\n';
    }
    // calculo:
    float valor;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < p; j++)
        {
            valor = 0.0;
            for (int k = 0; k < m; k++)
            {
                valor = valor + A[i * m + k] * B[k * p + j];
                // A[i][k]* A[k][j]
            }
            C[i*p + j] = valor;            
        }
    }
    // valores de C
    cout << "Matriz C:" << '\n';
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            cout << C[i*p + j] << " ";
        }
        cout << '\n';
    }
}