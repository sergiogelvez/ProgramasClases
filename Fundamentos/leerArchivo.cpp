#include <iostream>
#include <fstream>

using namespace std;

// "age.at.death";"age";"alive";"male";"height";"weight"
typedef struct registro
{  
    float edad;
    float estatura;
    float peso;
}registro;

int main()
{
    string nombre, linea;
    cout << "introduzca el nombre del archivo a leer:";
    cin >> nombre;
    ifstream archivo;
    archivo.open(nombre);
    if (!archivo)
    {
        cerr << "Unable to open file " << nombre;
    }
    else
    {
        int linea = 0, ltotal;
        archivo >> ltotal;
        registro reg[ltotal];
        while (linea < ltotal)
        {
            archivo >> reg[linea].edad >> reg[linea].estatura >> reg[linea].peso;
            linea++;
        }
        for (int i = 0; i < ltotal; i++)
        {
            cout << "Edad:" << reg[i].edad << " - Estatura:" << reg[i].estatura << " - Peso:" << reg[i].peso << endl;
        }
        

    }
    
}