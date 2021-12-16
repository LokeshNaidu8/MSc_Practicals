from random import choice, randint
from operator import eq

def get_sequences() -> tuple[list[str]]:
	char_sequence = 'ACTG'
	sequence_1 = [choice(char_sequence) for i in range(randint(10, 50))]
	sequence_2 = [choice(char_sequence) for i in range(randint(10, 50))]
	
	return sequence_1, sequence_2

def insert_gap(sequence : list[str]) -> list[str]:
	sequence.insert(randint(0, len(sequence) - 1), '-')
	
	return sequence

def insert_gaps(sequence_1 : list[str], sequence_2 : list[str]) -> tuple[list[str]]:
	while len(sequence_1) != len(sequence_2):
		if len(sequence_1) < len(sequence_2):
			sequence_1 = insert_gap(sequence_1)
		else:
			sequence_2 = insert_gap(sequence_2)
		
	return sequence_1, sequence_2

def pairwise_alignment(sequence_1 : list[str], sequence_2 : list[str]) -> list[str]:
	return list(map(eq, sequence_1, sequence_2))

if __name__ == "__main__":
	sequence_1, sequence_2 = get_sequences()
	print("Sequence 1 is>\n", sequence_1)
	print("Sequence 2 is>\n", sequence_2)
	print("\n")
	
	sequence_1, sequence_2 = insert_gaps(sequence_1, sequence_2)
	print("Sequence 1 after adding gaps is>\n", sequence_1)
	print("Sequence 2 after adding gaps is>\n", sequence_2)
	print("\n")
	
	score_list = pairwise_alignment(sequence_1, sequence_2)
	print("Score list is>\n", [1 if i else 0 for i in score_list])
	print(f"Score is {sum(score_list)}")
