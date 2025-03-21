

list = [1, 3, 4, 5, 6]
list[0:4] = 'A'
print(list)
#import mcb185
import sequence
import sys
import math
#sequence = sys.argv[1]


def find_entropy(letters):
    Ac = 0
    Cc = 0
    Gc = 0
    Tc = 0
    for letter in letters:
        if letter == 'A' : Ac += 1
        if letter == 'C' : Cc += 1
        if letter == 'G' : Gc += 1
        if letter == 'T' : Tc += 1    
    pa = Ac/(len(letters))
    pc = Cc/(len(letters))
    pg = Gc/(len(letters))
    pt = Tc/(len(letters))
    if pa != 0:
        h = -pa*math.log2(pa)
    if pc != 0:
        h =-pc*math.log2(pc)
    return h



def mask_window():
    pass

#for defline, seq in mcb185.read_fasta(sequence):
seq = 'AAAAAAAAAAGTCCGTCCGGCT'
seq_list = []
og_seq = seq.split
for i in range(0, len(seq)- 11):
    window = seq [i:i + 10]
    if find_entropy(window) < 1.1:
        for j in range (len(window)):
            og_seq [i + j] = 'N'
print (''.join(og_seq))


