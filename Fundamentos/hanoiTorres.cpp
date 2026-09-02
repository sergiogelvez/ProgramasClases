#include <iostream>
#include <cstdlib>

void hanoi(int n, char src, char dest, char aux)
{
    if (n==1)
    {
        std::cout << "Moviendo disco " << n << " desde el poste " << src << " a el poste destino " << dest << std::endl;
        return; 
    }
    hanoi( n - 1, src, aux, dest);
    std::cout << "Moviendo disco " << n << " desde el poste " << src << " a el poste destino "<< dest << std::endl;
    hanoi( n - 1, aux, dest, src);
}

int main()
{
    int n = 4;
    hanoi(n,'A','B','C');
}