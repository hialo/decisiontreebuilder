#include "instance.h"

Instance::Instance(){}

Instance::Instance(vector<string> attributes) {
    this->attributes = attributes;
}

Instance::Instance(vector<string> attributes, int classification) {
    this->attributes = attributes;
    this->classification = classification;
}

int Instance::getClassification() {
    return this->classification;
}

vector<string> Instance::getAttributes() {
    return this->attributes;
}