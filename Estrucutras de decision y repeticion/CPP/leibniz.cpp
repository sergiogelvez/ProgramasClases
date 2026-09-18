#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
    int i, n;
    double suma;

    cin >> n;
    suma = 0;
    for (i = 0; i <= n; i++) {
        suma = suma + pow(-1, i) / (2 * i + 1);
    }
    cout << suma * 4 << endl;
    return 0;
}




