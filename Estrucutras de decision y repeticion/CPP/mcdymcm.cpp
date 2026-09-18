#include <iostream>

using namespace std;

int main()
{
    int num1, num2, mcd, mcm, i, limite, min;
    cout << "Cual es el primer numero?: ";
    cin >> num1;
    cout << "Cual es el segundo numero?: ";
    cin >> num2;
    if ((num1 % 2 == 0 && num2 % 2 == 0) || (num1 % 2 != 0 && num2 % 2 != 0))
    {
        // aca el mcd
        mcd = 1;
        if (num1 < num2)
        {
            limite = num1;
        }
        else
        {
            limite = num2;
        }

        for (i = 1; i <= limite; i++)
        {
            if (num1 % i == 0 && num2 % i == 0)
            {
                mcd = i;
            }
        }
        cout << "El mcd de " << num1 << " y " << num2 << " es " << mcd << endl;
    }
    else
    {
        // lo del mcm
        mcm = limite;
        limite = num1 * num2;
        if (num1 > num2)
        {
            min = num1;
        }
        else
        {
            min = num2;
        }
        for (i = limite; i >= min; i--)
        {
            if (i % num1 == 0 && i % num2 == 0)
            {
                mcm = i;
            }
        }
        cout << "El mcm de " << num1 << " y " << num2 << " es " << mcm << endl;

    }

}