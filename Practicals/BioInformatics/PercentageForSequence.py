import random

seq1 = input("Enter 1st Sequence (Type sequence as a string For eg: 'ALPLEV') : ").upper()  # Type sequence as 'TNLAOEC'
print('First sequence is : ', seq1)
seq2 = input("Enter 2nd Sequence : ").upper()  # Type sequence as 'TNLAOEC'
print('Second sequence is : ', seq2)

def CalculatePercentage(seq1, seq2):
    s1 = [i for i in seq1]
    s2 = [i for i in seq2]
    if (len(s1) != len(s2)):  # Condition to check whether to insert gap or not
        if (len(s1) > len(s2)):
            lendiff = len(s1) - len(s2)
            for i in range(lendiff):
                randomize = random.randrange(0, len(s2))
                s2.insert(randomize, '-')
        else:
            lendiff = len(s2) - len(s1)
            for i in range(lendiff):
                randomize = random.randrange(0, len(s1))
                s1.insert(randomize, '-')
    print("Sequence 1 : ", s1)  # After Gap values
    print("Sequence 2 : ", s2)  # After inserting Gap
    identity = 0
    identitylist = []
    for i in range(len(s1)):
        if (s1[i] == s2[i] and (s1[i] != '-' and s2[i] != '-')):
            identitylist.append([s1[i], s2[i]])
            identity += 1
    print('\nIdentity list is ', identitylist)
    print('Total identity is ', identity)

    print('\n----------------SIMILARITY-----------------')
    tryagain = True  # Similarity coding starts here
    while (tryagain == True):
        try:
            similarity = int(input('How many sequences you want to make similar , Please enter Number: '))
        except Exception as e:
            print('\n---------Error: ', e, '----------')
            print('*********Try again to enter a total amount of sequence**********\n')
            tryagain = True
        else:
            tryagain = False
    similarsequence = []
    for i in range(1, similarity + 1):
        simi1 = input(f'\nEnter similar value for similarity {i}, Enter only one character: ').upper()
        simi2 = input(f'What you want to make similary to {simi1} :').upper()
        similarsequence.append([simi1, simi2])
        print('Your similar sequence : ', similarsequence)

    totalsimilarity = 0
    for i in range(len(s1)):
        for j in similarsequence:
            if (j[0] == s1[i] or j[0] == s2[i] and j[1] == s1[i] or j[1] == s2[i]):
                totalsimilarity += 1
    print('\nTotal Similarity : ', totalsimilarity)

    if ('-' in s1):
        totalLength = len(s2)
        print('Taking Total length of seq2 as ', totalLength, ' because seq1 has gaps')
    else:
        totalLength = len(s1)
        print('Taking Total length of seq1 as ', totalLength, ' because seq2 has gaps')
    ObtainedMatch = identity + totalsimilarity
    print('Total obtained Match is : ', ObtainedMatch, '\n')
    return f'Percentage of 2 sequences are {ObtainedMatch / totalLength * 100}% '


print(CalculatePercentage(seq1,seq2))
