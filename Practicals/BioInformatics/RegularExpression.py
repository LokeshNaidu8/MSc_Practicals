from random import choice, randint
from string import ascii_uppercase

def get_sequences(no_of_sequences : int) -> list[list[str]]:
	sequence_list = []
	print("Enter the sequences (All sequences should have equal length)>\t")
	
	for i in range(no_of_sequences):
		sequence_list.append(list(input(f"Enter sequence {i + 1}>\t")))
	
	return sequence_list


def get_random_sequences(no_of_sequences : int) -> list[list[str]]:
	sequence_length = randint(8, 20)
	sequence_list = [[choice(ascii_uppercase[: 6]) for j in range(sequence_length)] for i in range(no_of_sequences)]
	return sequence_list


def get_regular_expression(sequence_list : list[list[str]]) -> list[str]:
	output_sequence = []
	
	for i in range(len(sequence_list[0])):
		char_column = set()
		
		for j in range(len(sequence_list)):
			if sequence_list[j][i] != '-':
				char_column.add(sequence_list[j][i])
		
		char_at_i = ""
		
		if len(char_column) == 1:
			char_at_i = char_column[0]
		
		else:
			if len(char_column) == len(sequence_list):
				char_at_i = 'X'
			else:
				char_at_i += "["
				for i in char_column:
					char_at_i += i
				char_at_i += "]"
		
		output_sequence.append(char_at_i)
	
	return output_sequence

if __name__ == "__main__":
	print("Regular Expression in Python 3.6+")
	no_of_sequences = int(input("Enter the number of input sequences>\t"))
	
	random_flag = False if input("Do you want the sequences to be randomly generated? [Yes]/No>\t").lower() == "no" else True
	sequence_list = get_random_sequences(no_of_sequences) if random_flag else get_sequences(no_of_sequences)
	
	print("Sequences are as follows:")
	for i in range(len(sequence_list)):
		print(f"Sequence {i + 1}>\t", sequence_list[i])
	
	print("Regular expression for given sequences is:\t", get_regular_expression(sequence_list))
