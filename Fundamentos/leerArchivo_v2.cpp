#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

typedef struct registro
{
    string id;
    string nombres;
    string apellidos;
    int salarioBase;
    int horasExtra;
    int valorHoraBase;
}reg;

int main(int argc, char** argv)
{
    vector<reg> listado;
    reg elemento;
    string nombre, linea;
    nombre = "nomina1.txt";
    ifstream archivo;
    archivo.open(nombre);
    int contLineas = 0;
    if (!archivo)
    {
        cout << "Archivo inválido.";
    }
    else
    {
    while (getline(archivo, linea))
        {
            contLineas++;
            // Se imprime la línea completa
            cout << "Linea número " << contLineas << " : " << linea << endl;
            // Acá se divide la línea por los separadores
            char separador = ';';
            stringstream ssLinea(linea);
            string token;
            // acá se separa cada linea en los elementos entre los puntos y coma
            int contTokens = 0; 
            while (getline(ssLinea, token, separador))
            {
                if (contTokens == 0) { elemento.id = token; }
                if (contTokens == 1) { elemento.apellidos = token; }
                if (contTokens == 2) { elemento.nombres = token; }
                if (contTokens == 3) 
                {
                    elemento.salarioBase = stoi(token);
                    elemento.valorHoraBase = elemento.salarioBase / (30 * 8); 
                }
                if (contTokens == 4) { elemento.horasExtra = stoi(token); }
                contTokens++;
                // cout << token << endl;
            }
            listado.push_back(elemento);
            // acá se arma el registro entero, es un <<listado>> de <<elementos>>
        }
        // acá se hace el resto del proceso: Hacer operaciones, imprimir, mandar a archivo, etc
        cout << "Procesando " << contLineas << " registros..." << endl;
        ofstream archivoS;
        archivoS.open("salidacpp.csv");
        int i = 0;
        while ( i < contLineas)
        {
            archivoS << listado[i].id << ";" << listado[i].nombres + " " + listado[i].apellidos << ";" << listado[i].valorHoraBase << endl;
            cout << listado[i].id << ";" << listado[i].nombres + " " + listado[i].apellidos << ";" << listado[i].valorHoraBase << endl;
            i++;
        }
    }   
}