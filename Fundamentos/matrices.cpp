#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

/* void imprimirMatriz(int n, int m, int v[][m])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << v[i][j] << " ";
        }
        cout << '\n';
    }
} */

int main()
{
    int n, m, p;
    cout << "Introduzca los valor de n, m, p " << '\n';
    cin >> n;
    cin >> m;
    cin >> p;
    float A[n][m], B[m][p], C[n][p];
    srand(time(0));
    int i, j;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            A[i][j] = rand() % 10;            
        }
    }
    // matriz B
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < p; j++)
        {
            B[i][j] = rand() % 10;            
        }
    }
    // imprimirMatriz(n, m, A);
    cout << "Matriz A:" << '\n';
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << A[i][j] << " ";
        }
        cout << '\n';
    }
    cout << "Matriz B:" << '\n';
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++)
        {
            cout << B[i][j] << " ";
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
                valor = valor + A[i][k] * B[k][j];
            }
            C[i][j] = valor;            
        }
    }
    // valores de C
    cout << "Matriz C:" << '\n';
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            cout << C[i][j] << " ";
        }
        cout << '\n';
    }
}