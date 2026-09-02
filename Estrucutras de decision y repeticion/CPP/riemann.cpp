#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

float f(float x)
{
    return cos(x);
}

int main(int argc, char *argv[]) 
{
    int n;
    float a, b; // el orden en línea de comando es a b n 
    if (argc > 1)
    {
        a = stof(argv[1]);
        b = stof(argv[2]);
        n = stoi(argv[3]);
    }
    else
    {
        n = 100;
        a = 0;
        b = M_PI;
    }
    if (a < b && n > 1)
    {
        int vec[n + 1];
        float dx = (b - a) / n;
        float sum = 0, term = 0;
        for (int i = 0; i < n + 1; i++)
        {
            term = f(a + i*dx) * dx;
            sum += term;
            vec[i] = term;
            cout << "x = " << a + i*dx << " ; f(x) = " << f(a + i*dx) << endl;
        }
        cout << endl << "El valor aproximado de la integral es " << sum;
    }
    else
    {
        cout << "Parametros incorrectos, fin del programa" << endl;
    }
}