import random


class MultipleSeq:
    def __init__(self):
        try:
            howmany = int(input("How many number of sequence do you want (Enter Integer values) : "))
        except Exception as e:
            print('\n\nError : ', e)
        self.sequenceList = []
        self.length = []
        for i in range(1, howmany + 1):
            seq = input(f'Enter sequence {i} : ').upper()  # Example : 'AOSLIE'
            self.length.append(len(seq))
            self.sequenceList.append([i for i in seq])

    def gap(self):  # Insert gap
        maxlength = max(self.length)
        aftergapseq = []
        for i in self.sequenceList:
            if len(i) < maxlength:
                difflength = maxlength - len(i)
                for gapper in range(difflength):
                    r = random.randrange(0, len(i), 1)
                    i.insert(r, '-')
                aftergapseq.append(i)
            else:
                aftergapseq.append(i)
        print("After inserting gaps : \n", aftergapseq)
        return aftergapseq

    def multipleSequenceAlignment(self):
        sequence = self.gap()
        seq = []
        for i in range(len(sequence[0])):
            innerseq = []
            for j in sequence:
                innerseq.append(j[i])
            seq.append(innerseq)
        print("\nMultiple Sequence Calculation\n", seq)
        resulter = []
        maxer = []
        for i in seq:
            innerresult = []
            innermax = []
            for j in i:
                if j != '-':
                    counter = i.count(j)
                    innermax.append(counter)
                    tur = (j, counter)
                    innerresult.append(tur)
            resulter.append(innerresult)
            maxer.append(innermax)
        result = []

        for i in range(len(maxer)):
            maximum = max(maxer[i])
            ir = set()
            for j in resulter[i]:
                if (maximum == j[1]):
                    ir.add(j[0])
            result.append(ir)
        maxerset = []
        for i in maxer:
            setter = set()
            for j in i:
                setter.add(j)
            maxerset.append(setter)

        lastlist = []
        for i in range(len(maxerset)):
            stp = ''
            if (len(maxerset[i]) > 1):
                for k in result[i]:
                    stp = stp + k.lower()
            else:
                for k in result[i]:
                    stp = stp + k.upper()
            lastlist.append(stp)
        print("\n------------------The Result is----------------\n", lastlist)


myseq = MultipleSeq()
myseq.multipleSequenceAlignment()
