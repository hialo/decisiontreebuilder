#include "filemanager.h"

FileManager::FileManager(){}

void FileManager::openingFile (const string filepath, ifstream& file){
    cout << "Opening file..." << endl;

    file.open (filepath.c_str());

    if(!file.is_open()) {
        cout << "Impossible to open the file!" << endl;
        exit(-1);
    }
}

/****************************************************************/

void FileManager::writingFile (string text, string type){
	ofstream output;
	type += ".csv";

	const char* filepath = type.c_str();

	output.open (filepath);

	output << text;

	output.close();
}

/****************************************************************/

int FileManager::gettingFileSize(const string filepath){
    int size = 0;
    string line;

    ifstream file;
    openingFile(filepath, file);

    while (getline(file, line))
        size++;

    cout << "File size: " << size << " lines." << endl;

    file.close();

    return size;
}

/****************************************************************
* Esta função recebe as instâncias e o nome do arquivo, e gera um novo vetor
* com as instâncias misturadas. Então, a função generatingRandomTests() é
* chamada para criar os k folds e escrevê-los em novos arquivos.

* This function receives the instances and the filepath, and generates
* a new vector with the shuffled instances. Then, it calls generatingRandomTests() to
* write the k folds accordingly.
****************************************************************/

void FileManager::kfoldTests (int k, vector <Instance>& instances, const string filepath){
    int size = gettingFileSize(filepath);
    int index = 0;
    int var;

    vector<string> kfold (k);
    string line;

    bool* control = new bool[size];
    srand(time(NULL));

    for (int i = 0; i < size; i++)
        control[i] = false;

    cout << "Generating " << k << "-fold tests..." << endl;

    while (index != size){
        var = rand() % size;

        if (!control[var]){
            vector<string> temp = instances[var].getAttributes();
            line = "";

            for (unsigned int i = 0; i < temp.size(); i++){
                line += temp[i] + ",";
            }

            line += to_string(instances[var].getClassification());

            kfold[index % k] += line + "\n";

            control[var] = true;
            index++;
        }
    }

    cout << "Done." << endl;

    generatingRandomTests(kfold);
}

/****************************************************************/

void FileManager::generatingRandomTests(const vector<string>& kfold){
    string training;
    string testing;

    for (unsigned int i = 0; i < kfold.size(); i++){
        training = "";
        testing = "";

        for (unsigned int j = 0; j < kfold.size(); j++){
            if (i == j)
                testing += kfold[j];
            else
                training += kfold[j];
        }

        writingFile(training, "training_" + to_string(i));
        writingFile(testing, "testing_" + to_string(i));
    }
}


/****************************************************************/

vector <Instance> FileManager::readingFile(const string filepath){
	vector <Instance> set;
	ifstream file (filepath.c_str());

	string line;
	string i;

	if(!file.is_open()) {
        cout << "Impossible to open the file!" << endl;
        exit(-1);
    }

    while (getline(file, line)){
    	stringstream ss (line);
    	vector<string> attrib;
        int classif;

        while (getline(ss, i, ',')){
            attrib.push_back(i);

            //if (ss.peek() == ',')
            //  ss.ignore();
        }

        stringstream iss;
        i = attrib.back();
        attrib.pop_back();

        iss << i; //class
    	iss >> classif;

    	Instance in = Instance (attrib, classif);

    	set.push_back(in);
    }

    file.close();

    return set;
}