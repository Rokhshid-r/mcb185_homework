
import mcb185
import sequence
import sys
sequence = sys.argv[1] #'ACGTACGTGGGGGACGTACGTCCCCC'
w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sequence):
    w1 = seq[0:w]
    c = w1.count('C')
    g = w1.count('G')
    init_gc = c + g
    for i in range(0, len(seq) -w ):
        if w1[0] == 'C':
            if seq[w+i] == 'C': continue
            elif seq[w+i] == 'G': g += 1; c -= 1
            c -= 1
        if w1[0] == 'G':
            if seq[w+i] == 'G': continue
            elif seq[w+i] == 'C': g += 1; c -= 1
            c -= 1
        if w1[0] == 'A' or 'T':
            if seq[w+i] == 'C': c += 1
            elif seq[w+i] == 'G': g += 1
        w1 = w1[1:] + seq[w + i]
        print ((g+c)/ w)
        if c + g == 0: print(0)
        else: print((g - c)/ (g + c))

#17:08