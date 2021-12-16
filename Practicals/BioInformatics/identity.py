from random import choice, randint

def get_sequences() -> tuple[list[str]]:
	char_sequence = 'ACTG'
	sequence_length = randint(10, 20)
	sequence_1 = [choice(char_sequence) for i in range(sequence_length)]
	sequence_2 = [choice(char_sequence) for i in range(sequence_length)]
	
	return sequence_1, sequence_2

def identity(sequence_1 : list[str], sequence_2 : list[str]) -> tuple[int, list[list[int]]]:
	
	result_matrix = [[1 if i == j else 0 for j in sequence_1] for i in sequence_2]
	result = sum([sum(i) for i in result_matrix])
	
	return result, result_matrix

def print_matrix(matrix : list[list[int]]):
	for i in matrix:
		print(i)
	print()


if __name__ == "__main__":
	sequence_1, sequence_2 = get_sequences()
	print("Sequence 1 is>\n", sequence_1)
	print("Sequence 2 is>\n", sequence_2)
	print("\n")
	
	result, result_matrix = identity(sequence_1, sequence_2)
	print("Result matrix is>\n")
	print_matrix(result_matrix)
	print(f"Identity is {round((result / (len(sequence_1) * len(sequence_2))) * 100, 2)}")
