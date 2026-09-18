#include <iostream>

using namespace std;

int main()
{
    int i, n, ultimo = 1, penultimo = 0, suma;
    cout << "Numero de términos de fibonacci a calcular: ";
    cin >> n;
    cout << penultimo << ", ";
    cout << ultimo << ", ";
    for (i = 0; i < n; i++)
    {
        suma = ultimo + penultimo;
        penultimo = ultimo;
        ultimo = suma;
        cout << suma;
        if (i != n - 1)
        {
            cout << ", ";
        }
    }
}