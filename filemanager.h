#ifndef FILEMANAGER_H
#define FILEMANAGER_H

#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <cmath>
#include <string>
#include "instance.h"
#include "filemanager.h"

using namespace std;

class FileManager {
  public:
    FileManager();

    void openingFile (const string filepath, ifstream& file);
    void writingFile (string text, string type);
    vector <Instance> readingFile(const string filepath);
    void kfoldTests (int k, vector <Instance>& instances, const string filepath);
    void generatingRandomTests(const vector<string>& kfold);
    int gettingFileSize(const string filepath);
};

#endif