import random


class Similarity:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.s1 = []
        for i in seq1:
            self.s1.append(i)
        self.s2 = []
        for i in seq2:
            self.s2.append(i)

    def __repr__(self):
        return f"SEQUENCE 1: {self.seq1}\nSEQUENCE 2: {self.seq2}"

    def gap(self):
        if len(self.seq1) != len(self.seq2):
            if len(self.seq1) > len(self.seq2):
                howmanygaps = len(self.seq1) - len(self.seq2)
                for i in range(howmanygaps):
                    self.s2.insert(random.randrange(0, len(self.seq1), 1), '-')
                return [self.s1, self.s2]
            else:
                howmanygaps = len(self.seq2) - len(self.seq1)
                for i in range(howmanygaps):
                    self.s1.insert(random.randrange(0, len(self.s1), 1), '-')
                return [self.s1, self.s2]
        else:
            return [self.s1, self.s2]

    def checkSimilarity(self):
        similarJunction = []
        q = 'y'
        while (q == 'y'):
            sim1 = input("Enter a element that is going to be similar (String) : ")
            similarJunction.append(sim1)
            howMany = int(input('How many elements is going to be similar (Number) :'))
            for i in range(howMany):
                sim2 = input(f"What are those elements that are similar to {sim1} : ")
                similarJunction.append(sim2)

            q = input('Do you want to make another pair of similar values .\nSay y/n ? : ')
        return similarJunction


s = Similarity('actgat', 'gctaagtc')

print(s.checkSimilarity())
