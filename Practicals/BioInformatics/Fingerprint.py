class Fingerprint:
    def __init__(self, seq):
        self.allSeq = seq

    def __str__(self):
        return f"{self.allSeq}"

    def fingerprint(self):
        length = len(self.allSeq[0])

        sequence = []
        for i in range(length):  # 1-6
            innerseq = []
            for j in range(len(self.allSeq)):  # 1-3
                innerseq.append(self.allSeq[j][i])
            sequence.append(innerseq)
        print("\nSequence for fingerprint is \n", sequence)

        fp = {}
        for i in range(len(sequence)):
            A = sequence[i].count('A')
            T = sequence[i].count('T')
            G = sequence[i].count('G')
            C = sequence[i].count('C')
            gt = {"A": A, "T": T, "G": G, "C": C}
            fp[i + 1] = gt

        print(fp)
        for key, value in fp.items():
            print(f"--------{key}---------")
            for i, j in value.items():
                print(i, ":", j)

        print()
        print("A T G C")
        for key, value in fp.items():
            for i, j in value.items():
                print(j,end=" ")
            print()

def seq():
    again = True
    while (again != False):
        try:
            n = int(input("Enter how many sequence you want (Integer only): "))
        except Exception as e:
            print(f"\n*************** {e} *****************\nTry again :(\n")
            again = True
        else:
            again = False

    lengthagain = True
    while (lengthagain != False):
        try:
            length = int(input("Please tell us the length of the sequence : "))
        except Exception as e:
            print(f"\n*************** {e} *****************\nTry again :(\n")
            lengthagain = True
        else:
            lengthagain = False

    allSeq = []
    valid = 'ATGC'  # Sequence should contain only 'ATGC'
    print('\n*#*#*#*#\nREMEMBER: Sequence should only contain "ATGC" letters on it\n'
          'IF not SEQUENCE will be DISCARDED\n*#*#*#*\n')
    for i in range(n):
        tryagain = True
        while (tryagain != False):
            sequence = input(f'Enter seq {i + 1} : ').upper()  # Enter only ATGC
            for j in sequence:  # Validating the sequence
                if j not in valid:
                    print("\n---------------Invalid sequence :(\nSequence should only contain 'ATGC'")
                    print("Try again\n")
                    tryagain = True
                    break
            else:
                if (len(sequence) == length):  # Checking the length
                    tryagain = False
                    allSeq.append(sequence)
                else:
                    print("Invalid Length of your sequence \nTry again :(\n")
                    tryagain = True

        print(f"Your sequence {i + 1} is {sequence}")
    print(f"\nAll sequence = {allSeq}")
    return allSeq


'''Executing program'''
s = seq()
fingerprintObj = Fingerprint(s)
fingerprintObj.fingerprint()
