#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <string>

#include "instance.h"
#include "filemanager.h"

using namespace std;

/*********************************************************
* Este código cria os k folds necessários para executar Validação Cruzada 
* em uma base de dados. Separando as instâncias de forma randômica, este código
* gera os arquivos de treinamento e testes de acordo.

* This code creates k folds to execute cross-validation in a dataset.
* It shuffles the instances in a random way and creates new training and
* testing files.
*********************************************************/

int main (int argc, char* argv []){
	if(argc == 1) {
        cout << "ERROR: You need to pass the full dataset and k (./exec dataset k)." << endl;
    }

    if (argc == 3){
        string dataset = argv[1];
        int k = atoi(argv[2]);

        vector <Instance> data;

        FileManager fm;

        data = fm.readingFile(dataset);

        fm.kfoldTests(k, data, dataset);
    }

	return 0;
}