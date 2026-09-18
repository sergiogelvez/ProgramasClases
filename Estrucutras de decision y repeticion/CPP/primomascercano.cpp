#include <iostream>

using namespace std;

int main()
{
    int nlim, num, i, divisores, ultimoprimo = 2;
    bool encontrado = false;
    cout << "Ponga el numero limite porfa: ";
    cin >> nlim;
    num = nlim;
    while (encontrado == false) // (!encontrado)
    {
        divisores = 0;
        for (i = 2; i < num; i++)
        {
            if (num % i == 0)
            {
                divisores = divisores + 1;
            }
        }
        if (divisores == 0)
        {
            ultimoprimo = num;
            encontrado = true;
        } 
        else
        {
            num = num - 1;
        }

    }
    cout << "El primo más cercano a " << nlim << " es " << ultimoprimo << endl;
}
