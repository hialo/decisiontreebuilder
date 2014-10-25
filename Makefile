all:
	g++ -o exec main.cpp instance.cpp filemanager.cpp -W -Wall -ansi -pedantic -std=c++11
	echo 'USAGE: ./exec data_set k, where data_set is the dataset and k, the number of folds you need'

clean:
	rm KNN
