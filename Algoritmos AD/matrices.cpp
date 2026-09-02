#include <iostream>
#include <cmath>
#include <vector>
#include <stdlib.h>
#include <time.h>

using namespace std;

void mulMatLineal(double [], double [], double [], int , int, int, int);
void mulMatVector(vector <double> A, vector <double> B, vector <double> C, int, int, int, int);
void mulMatVector2(vector <double> A, vector <double> B, vector <double> &C, int, int, int, int);
vector <double> mulMatVector3(vector <double> A, vector <double> B, int, int, int, int);

void impMat(double A[], int n, int m)
{
    int i, j;
    for ( i = 0; i < n; i++)
    {
        for ( j = 0; j < m; j++)
        {
            cout << A[ i*m + j ] << " ";
        }
        cout << "\n";
    }
}

void impMatV(vector <double> A, int n, int m)
{
    int i, j;
    for ( i = 0; i < n; i++)
    {
        for ( j = 0; j < m; j++)
        {
            cout << A[ i*m + j ] << " ";
        }
        cout << "\n";
    }
}


int main()
{
    int n = 0, m = 0, p = 0, q = 0;
    int i, j, k;
    cout << "Introduzca el número de filas de la primera matriz: ";
    cin >> n;
    cout << "Introduzca el número de columnas de la primera matriz: ";
    cin >> m;
    cout << "Introduzca el número de filas de la segunda matriz: ";
    cin >> p;
    cout << "Introduzca el número de columnas de la segunda matriz: ";
    cin >> q;
    int nm = n*m, pq = p*q, nq = n*q;
    // inicializar los aleatorios
    // srand(time(0));
    if (m == p) 
    {
        cout << "Se generan las dos matrices con los parámetros provistos \n";
        // diferentes formas de generar las matrices
        // usando la estructura de C++
        vector <double> A1(nm) , B1(pq), C1(nq);
        // usando un array de una dimensión
        double A2[nm], B2[pq], C2[nq];
        // usando apuntadores
        double *A3, *B3, *C3;
        A3 = (double *) malloc ( nm * sizeof(double) );
        B3 = (double *) malloc ( pq * sizeof(double) );
        C3 = (double *) malloc ( nq * sizeof(double) );
        // usando matrices nativas de C
        double A4[n][m], B4[p][q], C4[n][q]; 
        // generar los valores de las matrices con números aleatorios
        double aleat;
        // generar A
        for (i = 0; i < n; i=i+1)
        {
            for (j = 0; j < m; j++)
            {
                aleat = rand() % 10;
                A1[ i * m + j] = aleat;
                A2[ i * m + j] = aleat;
                A3[ i * m + j] = aleat;
                A4[i][j] = aleat;

            }
        }
        // generar B
        for (i = 0; i < n; i=i+1)
        {
            for (j = 0; j < m; j++)
            {
                aleat = rand() % 10;
                B1[ i * m + j] = aleat;
                B2[ i * m + j] = aleat;
                B3[ i * m + j] = aleat;
                B4[i][j] = aleat;

            }
        }
        // imprimir As y Bs para mostrar que son identicas y que quedaron bien guardadas.
        cout << "Las diferentes versiones de A: \n";
        cout << "A1 (vectores de C++) \n";
        impMatV(A1, n, m);
        cout << "A2 (array de C de una dimensión) \n";
        impMat(A2, n, m);
        cout << "A3 (apuntadores) \n";
        impMat(A3, n, m);
        cout << "A4 (martrices de C) \n";
        for ( i = 0; i < n; i++)
        {
            for ( j = 0; j < m; j++)
            {
                cout << A4[i][j] << " ";
            }
            cout << "\n";
        }
        cout << "Las diferentes versiones de B: \n";
        cout << "B1 (vectores de C++) \n";
        impMatV(B1, p, q);
        cout << "B2 (array de C de una dimensión) \n";
        impMat(B2, p, q);
        cout << "B3 (apuntadores) \n";
        impMat(B3, p, q);
        cout << "B4 (martrices de C) \n";
        for ( i = 0; i < p; i++)
        {
            for ( j = 0; j < q; j++)
            {
                cout << B4[i][j] << " ";
            }
            cout << "\n";
        }
        // Multiplicar, primero la versión de matrices de C
        // mulMatVector(A1, B1, C1, n, m, p, q);
        C1 = mulMatVector3(A1, B1, n, m, p, q);
        mulMatLineal(A2, B2, C2, n, m, p, q);
        mulMatLineal(A3, B3, C3, n, m, p, q);
        // se preguntaran aquellos que lean este código por que no usé una función acá
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < q; j++)
            {
                double valorc = 0.0;
                for (k = 0; k < m; k++)
                {
                    valorc = valorc + A4[i][k] * B4[k][j];
                }
                C4[i][j] = valorc;
            }
        } 
        cout << "El resultado es: \n";
        cout << "C1 \n";
        impMatV(C1, n, q);
        cout << "C2 \n";
        impMat(C2, n, q);
        cout << "C3 \n";
        impMat(C3, n, q);
        cout << "C4 (martrices de C) \n";
        for ( i = 0; i < n; i++)
        {
            for ( j = 0; j < q; j++)
            {
                cout << C4[i][j] << " ";
            }
            cout << "\n";
        }
        // fin
    }
    else
    {
        cout << "No se puede hacer la multiplicación, el número de columnas de A es diferente al número de filas de B ( " << m << " , " << p << " ) ";
        cout << endl;
    }
}


void mulMatLineal(double A[], double B[], double C[], int n, int m, int p, int q)
{
    int i, j, k;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < q; j++)
        {
            double valorc = 0.0;
            for (k = 0; k < m; k++)
            {
                valorc = valorc + A[ i * m + k] * B[ k * m + j];
            }
            C[i*q + j] = valorc;
        }
    }
}

void mulMatVector(vector <double> A, vector <double> B, vector <double> C, int n, int m, int p, int q)
{
    int i, j, k;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < q; j++)
        {
            double valorc = 0.0;
            for (k = 0; k < m; k++)
            {
                valorc = valorc + A[ i * m + k] * B[ k * m + j];
            }
            C[i*q + j] = valorc;
        }
    }
}

void mulMatVector2(vector <double> A, vector <double> B, vector <double> &C, int n, int m, int p, int q)
{
    int i, j, k;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < q; j++)
        {
            double valorc = 0.0;
            for (k = 0; k < m; k++)
            {
                valorc = valorc + A[ i * m + k] * B[ k * m + j];
            }
            C[i*q + j] = valorc;
        }
    }
}

vector <double> mulMatVector3(vector <double> A, vector <double> B, int n, int m, int p, int q)
{
    int i, j, k;
    vector <double> C (n*q);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < q; j++)
        {
            double valorc = 0.0;
            for (k = 0; k < m; k++)
            {
                valorc = valorc + A[ i * m + k] * B[ k * m + j];
            }
            C[i*q + j] = valorc;
        }
    }
    return C;
}