#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int fact(int x)
{
    int prod = 1, i;
    for (i = 1; i <= x; i++)
    {
        prod = prod * i;
    }
    return prod;
}

int main()
{
    int n, i, angulo;
    float x, suma = 0.0;
    cout << "valor de n (terminos)?: ";
    cin >> n;
    cout << "Angulo (grados)?: ";
    cin >> angulo;
    x = (3.14159/180) * angulo;
    for (i = 0; i <= n; i++)
    {
        suma = suma + ((pow(-1, i)) * (pow(x, 2*i + 1)) ) / (fact(2 * i + 1));
    }    
    cout << "Seno de " << angulo << " es igual a: " << setprecision(20) << suma << endl;
    cout << "Seno de " << angulo << " es igual a: " << setprecision(20) << sin(x) << endl;

    
}

