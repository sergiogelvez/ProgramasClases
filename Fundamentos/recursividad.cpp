#include <iostream>

using namespace std;

int mcd(int a, int b)
{
    if (a == 0 || b == 0)
        return 0;
    else if (a == b)
        return a;
    else if (a > b)
        return mcd(a-b, b);
    else 
        return mcd(a, b-a);
}

int main()
{
    int a, b, result;
    cin >> a;
    cin >> b;
    result = mcd(a, b);
    if (result > 0)
    {
        cout << "El Máximo Común Divisor de " << a << " y " << b << " es: " << result << endl;
    }
    else
    {
        cout << "Error bien raro" << endl;
    }
    

}