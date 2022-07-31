#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    string myText;

    ifstream MyReadFile("/usr/src/app/staticfiles/filesize");

    while (getline(MyReadFile, myText))
    {
        cout << myText;
    }

    MyReadFile.close();
}