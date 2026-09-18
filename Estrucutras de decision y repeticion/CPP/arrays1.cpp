#include <iostream>

using namespace std;

int main()
{
    int n, i;
    cout << "Numero de elementos a promediar: ";
    cin >> n;
    float notas[n+1], suma = 0;
    for (i = 0; i < n; i++)
    {
        cout << "elemento " << i + 1 << ":";
        cin >> notas[i];
    }

    for (i = 0; i < n + 1; i++)
    {
        cout << notas[i] << ", ";
        suma = suma + notas[i];
    }

    cout << " El resultado es: " << suma / n;

}