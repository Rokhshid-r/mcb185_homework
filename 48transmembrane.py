

import sys
import gzip
import mcb185

kd_dict = {'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5}


def avg_kd(seq):
    sum = 0
    for aa in seq:
        aa_hydro = kd_dict[aa]
        sum +=aa_hydro
    return sum/len(seq)

    #I wasn't sure what window size to use but google said the KD measure works best for 5-7 window but only 7 matched your output.
def is_signal(seq):
    segment = seq[:30]
    for i in range(0, len(segment) -7):
        window = segment[i:i+8]
        if avg_kd(window) >= 2.5 and "P" not in window: return True
    return False

def is_transmembrane(seq):
    segment = seq[30:]
    for i in range(0, len(segment) - 10):
        window = segment[i: i+11]
        if avg_kd(window)>= 2.0 and 'P' not in window:
            return True
    return False


filename = sys.argv[1]
for defline, seq in mcb185.read_fasta(filename):
        if len(seq) >= 41:
            if is_signal(seq) == True and is_transmembrane(seq) == True:
                print(defline)

