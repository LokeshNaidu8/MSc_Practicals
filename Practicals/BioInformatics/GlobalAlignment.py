
class GlobalAlignment:
    gap = -2
    mismatch = -1
    match = 1

    def __init__(self, seq1, seq2):
        self.s1 = seq1
        self.s2 = seq2

    def __repr__(self):
        return f"Sequence 1 : {self.s1}\nSequence 2: {self.s2}"

    def matrix(self):
        matrix = []
        start = 0
        anotherstart = -2
        for i in range(len(self.s2) + 1):
            submatrix = []
            for j in range(len(self.s1) + 1):
                if i == 0:
                    submatrix.append(start)
                    start -= 2
                elif j == 0 and i != 0:
                    submatrix.append(anotherstart)
                    anotherstart -= 2
                else:
                    submatrix.append(0)
            matrix.append(submatrix)
        return matrix

    @staticmethod
    def beside(value):
        return value + GlobalAlignment.gap

    @staticmethod
    def up(value):
        return value + GlobalAlignment.gap

    def align(self):
        alignMatrix = []
        matrix = self.matrix()
        print(matrix)
        for i in range(1, len(matrix)):
            submatrix = []
            for j in range(1, len(matrix[i])):
                besides = GlobalAlignment.beside(matrix[i][j - 1])  # Beside value
                print('beside value: ', besides, " ", matrix[i][j - 1])
                dg = matrix[i - 1][j - 1]
                if self.s1[j - 1] == self.s2[i - 1]:
                    diagonal = dg + GlobalAlignment.match  # Beside value on match
                else:
                    diagonal = dg + GlobalAlignment.mismatch  # Diagonal value o mismatch
                print('diagonal value: ', diagonal)

                up = GlobalAlignment.up(matrix[i - 1][j])  # Up value
                print('up value: ', up)
                check = [besides, diagonal, up]
                maximum = max(check)
                print(maximum)
                ind = check.index(maximum)
                if ind == 0:
                    path = 'beside'
                elif ind == 1:
                    path = 'diagonal'
                elif ind == 2:
                    path == 'up'
                submatrix.append([maximum, path])
                matrix[i][j] = maximum
            alignMatrix.append(submatrix)
        print(alignMatrix)
        print("Matrix is ", matrix)
        return [matrix, alignMatrix]

    def traceback(self):
        originalmatrix = self.align()[0]
        tracingmatrix = self.align()[1]
        print("\nInside traceback\n",originalmatrix,"\n\n",tracingmatrix)


gb = GlobalAlignment('ATCG', 'GCT')
gb.traceback()