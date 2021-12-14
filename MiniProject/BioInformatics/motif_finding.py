# Leishmania donovani strain MHOM/IN/1980/DD8 Nucleoside hydrolase 1 (nh1)
import random
import re
f = open('motifseq.txt', 'r')
file=f.read()
randomvalue=random.randint(0,len(file)-5)

i=5
myseq=file[randomvalue:randomvalue+5]

print('Acquire sequence is', myseq)

allseq=re.findall(myseq,file)
if len(allseq)==1:
    print('No other seq found related to',myseq)
else:
    print(len(allseq)-1, f'{myseq} sequence found in our given file')