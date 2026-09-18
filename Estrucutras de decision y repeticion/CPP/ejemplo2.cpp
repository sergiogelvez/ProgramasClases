#include <iostream>

using namespace std;

int main()
{
    char opcion;
    cout << "Seleccione (A/B/C): ";
    cin >> opcion;
    switch (opcion)
    {
        case 'A' : cout << "Opción A seleccionada" << endl;
        break;
        case 'B' : cout << "Opción B seleccionada" << endl;
        break;
        case 'C': cout << "Opción C seleccionada" << endl;
        break;
        default : cout << "Opción no válida" << endl;
    }
}