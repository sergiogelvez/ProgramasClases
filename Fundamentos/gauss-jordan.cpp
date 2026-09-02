#include <iostream>
#include <cstdlib>

using namespace std;

double** gauss_jordan(double ** A, int n, int m);

double** gauss_jordan(double ** A, int n, int m)
{
	// se fija una fila para hallar los valores de los factores
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			// i es la fila fija y j es la fila a comparar y reducir
			if (i != j)
			{
				cout << "Fila fija = " << i << endl;
				
			}
		}
		

	}
}

void mostrar_matriz(double ** A, int n, int m)
{
	// A es la matriz aumentada, n el n�mero de filas y m el n�mero de columnas
	for (int i = 0; i < n; i++)
	{
		cout << " [ ";
		for (int j = 0; j < m; j++)
		{
			cout << A[i][j];
			if (j != m - 1)
				cout << ", ";
		}
		cout << " ] " << endl;
	}
}

int main()
{
	int filas, cols;
	cout << "Por favor introduzca el n�mero de filas de la matriz del sistema de ecuaciones: ";
	cin >> filas;
	cols = filas + 1;
	// double matriz[filas][cols];

	double** matriz = new double*[filas];
 
    for (int i = 0; i < filas; i++) {
 
        // Declare a memory block
        // of size n
        matriz[i] = new double[cols];
    }


	for (int i = 0; i < filas; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			cout << "Introduzca el valor para la posici�n (" << i << ", " << j << ") de la matriz: ";
			cin >> matriz[i][j];
			
		}
	}

	mostrar_matriz(matriz, filas, cols);
}