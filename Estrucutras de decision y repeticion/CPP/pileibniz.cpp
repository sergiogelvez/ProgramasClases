#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
    int n, i;
    double suma = 0, err, pi;
    cout << "Por favor introduzca el número de términos: ";
    cin >> n;
    for (i = 0; i <= n; i++)
    {
        suma = suma + pow(-1, i) / (2 * i + 1);
    }
    pi =  4 * suma;
    cout << "El valor de pi (calculado) es: " << setprecision(20) << pi << endl;
    cout << "El valor de pi (stadard) es: " << setprecision(20) << M_PI <<  endl;
    err = ((pi - M_PI) / M_PI ) * 100;
    cout << "El error es: " << err << "%" << endl;
}