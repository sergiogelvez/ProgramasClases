// https://cplusplus.com/doc/tutorial/files/
// https://www.scaler.com/topics/cpp-read-file-line-by-line/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    fstream new_file;
    
    // Open a file to perform a write operation using a file object.
    new_file.open("xyz.txt", ios::out); 
    
    // Checking whether the file is open.
    if (new_file.is_open()) {
        new_file << "My Function \n"; // Inserting text.
        new_file.close(); // Close the file object.
    }
    
    // open a file to perform read operation using file object.
    new_file.open("xyz.txt", ios::in); 
    
    // Checking whether the file is open.
    if (new_file.is_open()) { 
        string sa;
        // Read data from the file object and put it into a string.
        while (getline(new_file, sa)) { 
            // Print the data of the string.
            cout << sa << "\n"; 
        }
        
        // Close the file object.
        new_file.close(); 
    }
}
