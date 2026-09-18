#include <iostream>

using namespace std;

int main()
{
    int num, contneg = 0, contpos = 0; 
    float sumaneg = 0, sumapos = 0, promneg, prompos;
    num = -1;
    while (num != 0)
    {
        cout << "Deme el valor: ";
        cin >> num;
        if (num > 0) 
        {
            cout << "Positivo" << endl;
            sumapos = sumapos + num;
            contpos = contpos + 1;
        }
        else
        {
            if (num < 0)
            {
                cout << "Es negativo" << endl;
                sumaneg = sumaneg + num;
                contneg = contneg + 1;
            }
            else 
            {
                cout << "Fin del programa" << endl;
            }
        }
    }
    // mirar promedio positivos
    if (contpos > 0)
    {
        prompos = sumapos / contpos;
        cout << "El promedio de los positivos es " << prompos << " y hubo " << contpos << " enteros positivos" << endl;
    }
    else
    {
        cout << "No hubo valores positivos" << endl;
    }
    // mirar promedio negativos
    if (contneg > 0)
    {
        promneg = sumaneg / contneg;
        cout << "El promedio de los negativos es " << promneg << " y hubo " << contneg << " enteros negativos" << endl;
    }
    else
    {
        cout << "No hubo valores negativos" << endl;
    }
}