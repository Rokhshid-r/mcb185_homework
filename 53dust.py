
import argparse
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type = str, help = 'name of the fasta file')
parser.add_argument('--size', type = int, default= 20, help = 'window size [%(default)i]')
parser.add_argument('--entropy', type = float, default= 1.4, help = 'entropy threshold [%(default).3f]')
parser.add_argument('--lower', action = 'store_true', help = 'soft mask')

arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)


import mcb185
import sequence
import sys
import math


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
    if pa == 0: pa +=1
    if pt == 0: pt +=1
    if pc == 0: pc +=1
    if pg == 0: pg +=1
    h = -pa*math.log2(pa)-pc*math.log2(pc)-pt*math.log2(pt)-pg*math.log2(pg)
    return h



def mask_window():
    pass

for defline, seq in mcb185.read_fasta(arg.file):
#seq = 'AAAAAAAAAAGTCCGTCCGGCT'
    nt = ['A', 'B', 'C', 'D']
    seq_list = []
    og_seq = list(seq)
    for i in range(0, len(seq)- arg.size + 1):
        window = seq [i:i + arg.size]
        if find_entropy(window) < arg.entropy:
            for j in range (len(window)):
                letter = seq[i+j:i+j]
                og_seq [i + j] = letter.lower()
print (''.join(og_seq))
