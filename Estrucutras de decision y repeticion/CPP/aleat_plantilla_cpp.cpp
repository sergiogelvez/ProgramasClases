#include <iostream>
#include <vector>
#include <random>

int main()
{
    int n;
    std::cout << "Introduzca el número de elementos, por favor: ";
    std::cin >> n;

    // Generador de números aleatorios moderno
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 100);

    std::vector<int> elementos(n);
    
    // Generación de los n elementos con valores entre 1 y 100
    for (int i = 0; i < n; ++i)
    {
        elementos[i] = dis(gen);
    }

    // Impresión de los elementos
    for (int num : elementos)
    {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    std::cout << "Fin del programa\n";

    return 0;
}
