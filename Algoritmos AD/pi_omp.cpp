#include <iostream>
#include <chrono>
#include <omp.h>

int main()
{
    long long int i, n = 1000000000;
    double sum = 0;
    omp_set_num_threads(4);
    std::chrono::time_point<std::chrono::system_clock> t_inicio, t_final;
    t_inicio = std::chrono::system_clock::now();
    #pragma omp parallel for shared(n) reduction( + : sum ) 
    for ( i = 0; i < n; i++)
    {
        double factor = (i % 2 == 0) ? 1.0 : -1.0;
        sum += factor / (2 * i + 1);
    }
    t_final = std::chrono::system_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::milliseconds>(t_final - t_inicio).count();
    std::cout << "Tiempo transcurrido: " << t/1000.0 << std::endl;
}
