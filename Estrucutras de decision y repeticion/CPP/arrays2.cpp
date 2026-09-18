#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, i;
    cout << "Numero de elementos a promediar: ";
    cin >> n;
    float notas[n], suma = 0, promedio;
    for (i = 0; i < n; i++)
    {
        cout << "elemento " << i + 1 << ":";
        cin >> notas[i];
    }

    for (i = 0; i < n; i++)
    {
        cout << notas[i] << ", ";
        suma = suma + notas[i];
    }
    promedio = suma / n;
    cout << " El promedio es: " << promedio << endl;
    suma = 0;
    for (i = 0; i < n; i++)
    {
        suma = suma + pow(notas[i] - promedio, 2);
    }
    float var, desvest;
    // si es muestral cambiar denominador n por n - 1 
    var = suma / (n);
    desvest = sqrt(var);
    cout << "La varianza poblacional es " << var << " y la desviacion estandar es " << desvest << endl;
}