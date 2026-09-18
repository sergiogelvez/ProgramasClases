#include <iostream>
#include <vector>

int main()
{
    std::vector<float>notas;
    int i, n;
    float elem, suma, promedio;
    std::cout << "Cuantos elementos mugre quiere promediar: ";
    std::cin >> n;
    for (i = 0; i < n; i++)
    {
        std::cin >> elem;
        notas.push_back(elem);
    }

    // for "moderno" igual a:
    /*
    for (i = 0; i < notas.size(); i++)
    {
        std::cout << notas[i] << " ";
    }
    
    */
    for (float valor : notas)
    {
        std::cout << valor << " ";
    }

    std::cout << std::endl;
    suma = 0;
    for (i = 0; i < notas.size(); i++)
    {
        suma = suma + notas[i];
    }
    promedio = suma / notas.size();
    std::cout << "El promedio es " << promedio;
}



