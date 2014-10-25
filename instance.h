#ifndef INSTANCE_H
#define INSTANCE_H

using namespace std;

#include <vector>
#include <string>

class Instance {
  public:

    Instance();
    Instance(vector<string> attributes);
    Instance(vector<string> attributes, int classification);
    int getClassification();
    vector<string> getAttributes();

  private:

    vector<string> attributes;
    int classification;
};

#endif