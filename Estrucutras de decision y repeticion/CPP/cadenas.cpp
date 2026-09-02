#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>

using namespace std;

int main()
{
    string palabra1, palabra2;
    string texto, textoR;
    cout << "Escriba por favor el texto principal, para finalizar de enter" << endl;
    getline(std::cin, texto);
    cout << "El texto es:" << '\n' << texto << endl;
    cout << "Escriba por favor la palabra a buscar" << endl;
    cin >> palabra1;
    cout << "Escriba por favor la palabra a reemplazar" << endl;
    cin >> palabra2;
    textoR = texto;
    size_t pos = 0;
    string token;
    string delimitador = " ";
    vector<string> frase;
    while ((pos = textoR.find(delimitador)) != std::string::npos) {
        token = textoR.substr(0, pos);
        //std::cout << token << std::endl;
        frase.push_back(token);
        textoR.erase(0, pos + delimitador.length());
    }
    //std::cout << textoR << std::endl;
    frase.push_back(textoR);
    for (int i = 0; i < frase.size(); i++) 
    {
        cout << "\n" << frase.at(i) << "\n";
        if (frase.at(i) == palabra1)
        {
            cout << "\nJackpot: " << frase[i] << "\n";
            frase.at(i) = palabra2;
        }
    }
    stringstream res;
    copy(frase.begin(), frase.end(), ostream_iterator<string>(res, " "));
    textoR = res.str();
    cout << '\n' << "El nuevo texto es:" << '\n' << textoR << endl;

}

// El gato vuela por el bosque como el gato montez vuela por los cielos