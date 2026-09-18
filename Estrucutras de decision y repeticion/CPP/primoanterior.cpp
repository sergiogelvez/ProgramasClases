#include <iostream>

using namespace std;

int main()
{
    int nlim, num, i, divisores, ultimoprimo = 2;
    cout << "Ponga el numero limite porfa: ";
    cin >> nlim;
    for (num = 2; num <= nlim; num++)
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
        }

    }
    cout << "El primo más cercano a " << nlim << " es " << ultimoprimo << endl;
}
