// ConsoleApplication1.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include <cmath>
// #include <curses.h>

// se utilizara una función simple para las condiciones iniciales
// para las condiciones de frontera se usaran valores constantes

double uInicial(double x)
{
    return sin(x);
}

int main()
{
    std::cout << "Hola mundo, hoy vamos a simular la transferencia de calor en una barra ideal\n";
    std::cout << "En la dimensión x se varía la longitud y el dx, y en el tiempo el dt y el número de pasos \n";
    
    double dt = 0.1;
    int m = 100;
    int nsteps = 100;
    double largo = 200;
    double dx = largo / m;
    double tmax = nsteps * dt;
    std::cout << " El dx es " << dx << " el dt es " << dt << " y el tiempo máximo es " << tmax << " \n";

    // primera versión con valores duros
    if (dt <= (dx * dx) / 2)
    {
        std::cout << "los parametros de dx y dt son validos, se procede \n";

        double** U = new double* [m];
        for (int i = 0; i < m; i++)
        {
            U[i] = new double[nsteps];
        }

        for (int i = 0; i < m; i++)
        {
            U[i][0] = uInicial(i * dt);
        }

        // condiciones de frontera

        for (int j = 0; j < nsteps; j++)
        {
            U[0][j] = 0.0;
            U[m - 1][j] = 0.0;
        }

        // bucle principal
        for (int j = 1; j < nsteps; j++)
        {
            for (int i = 1; i < m - 1; i++)
            {
                // arreglar la relación
                U[i][j] = 1.0;
            }
        }

        for (int j = 0; j < nsteps; j++)
        {
            for (int i = 0; i < m; i++)
            {
                std::cout << U[i][j] << " ";
            }
            std::cout << "\n";
        }
    }
    else
    {
        std::cout << "Los parámetros de dx y dt no permiten la convergencia.  Fin del programa \n";
    }
}

// Ejecutar programa: Ctrl + F5 o menú Depurar > Iniciar sin depurar
// Depurar programa: F5 o menú Depurar > Iniciar depuración

// Sugerencias para primeros pasos: 1. Use la ventana del Explorador de soluciones para agregar y administrar archivos
//   2. Use la ventana de Team Explorer para conectar con el control de código fuente
//   3. Use la ventana de salida para ver la salida de compilación y otros mensajes
//   4. Use la ventana Lista de errores para ver los errores
//   5. Vaya a Proyecto > Agregar nuevo elemento para crear nuevos archivos de código, o a Proyecto > Agregar elemento existente para agregar archivos de código existentes al proyecto
//   6. En el futuro, para volver a abrir este proyecto, vaya a Archivo > Abrir > Proyecto y seleccione el archivo .sln
