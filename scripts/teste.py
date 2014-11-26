def full_tree():
	path = '/home/hialo/UnB/TCC2/codes/results/generated_trees/'
	var = 0;
	NUMBER_OF_CASES = 501;
	LINE = 4;

	for first_index in range (2, NUMBER_OF_CASES):
		var = 0

		full_path = path + str(first_index) + '/matrix.txt'

		f = open(full_path)
		lines = f.readlines()
		lines[LINE] = lines[LINE].split(": ")[1]

		lines[LINE] = lines[LINE].split("%")[0]
		print lines[LINE]

		f.close()

def conf():
	path = '/home/hialo/UnB/TCC2/codes/results/confidence/'
	var = 0;
	NUMBER_OF_CASES = 21;
	LINE = 4;

	for first_index in range (1, NUMBER_OF_CASES):
		var = 0

		full_path = path + str(first_index) + '/matrix.txt'

		f = open(full_path)
		lines = f.readlines()
		lines[LINE] = lines[LINE].split(": ")[1]

		lines[LINE] = lines[LINE].split("%")[0]

		print lines[2]
		print lines[LINE]

		f.close()

def kfold():
	path = '/home/hialo/UnB/TCC2/codes/results/generated_trees/'
	var = 0;
	NUMBER_OF_CASES = 1308;
	LINE = 10; 

	for first_index in range (3, NUMBER_OF_CASES):
		var = 0
		for second_index in range (0, first_index):
			full_path = path + str(first_index) + '/' + str(second_index) + '/matrix.txt'

			f = open(full_path)
			lines = f.readlines()
			lines[LINE] = lines[LINE].split(": ")[1]

			lines[LINE] = lines[LINE].split("%")[0]
			var += float(lines[LINE])

			f.close()

		print var/first_index

def roc():
	path = '/home/hialo/UnB/TCC2/codes/results/generated_trees/'

	for first_index in range (0, 10):
		for second_index in range (0, 10):
			full_path = path + str(first_index) + '/10/' + str(second_index) + '/matrix.txt'

			f = open(full_path)
			lines = f.readlines()

			print lines[13] + lines[14] 

			f.close()

def gettingAverageError():
	path = '/home/hialo/UnB/TCC2/codes/results/generated_trees/'
	total = 0
	NUMBER_OF_CASES = 10; 
	LINE = 10; #linha do arquivo aonde o percentual de erro dos testes se encontra

	for first_index in range (0, NUMBER_OF_CASES):
		var = 0
		for second_index in range (0, NUMBER_OF_CASES):
			full_path = path + str(first_index) + '/10/' + str(second_index) + '/matrix.txt'

			f = open(full_path)
			lines = f.readlines()
			lines[LINE] = lines[LINE].split(": ")[1]

			lines[LINE] = lines[LINE].split("%")[0]
			var += float(lines[LINE])

			f.close()

		total += var

	print total/NUMBER_OF_CASES*NUMBER_OF_CASES	

#kk()
conf()
#kfold()
#full_tree()
