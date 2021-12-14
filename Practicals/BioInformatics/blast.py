# import re
with open('Fasta.txt', 'r') as file:  # OC43 - Coronavirus
    # seq=re.sub('\n','',file.read())   #Removing all new lines from string
    # print(seq)
    seq = file.read()
    print(f"A->{seq.count('A')}\nT->{seq.count('T')}\nG->{seq.count('G')}\nC->{seq.count('C')}")
