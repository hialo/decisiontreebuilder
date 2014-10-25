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


/*********************************************************/

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

    /* for (unsigned int i = 0; i < 10; i++){
            vector<string> temp;

            temp = data[i].getAttributes();

            for (unsigned int j = 0; j < temp.size(); j++){
                cout << temp[j] << ",";
            }

            cout << data[i].getClassification() << endl;
        }*/

        fm.kfoldTests(k, data, dataset);
    }

	return 0;
}