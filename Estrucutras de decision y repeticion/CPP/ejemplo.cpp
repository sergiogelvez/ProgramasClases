#include <iostream>
#include <string>

using namespace std;

int main()
{ 
    string nombre;
    int edad;
    cout << "Ingrese su nombre:";
    cin >> nombre; // lee hasta espacio en blanco
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Hola," << nombre << ". Usted tiene " << edad << " años." << endl;
    return 0;
}