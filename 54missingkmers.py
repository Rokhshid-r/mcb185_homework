
"""
Write a program that searches sequences for the smallest missing k-mer. The program is a little different from 52kmercount.py.

Start k at 1 and increase until there are missing k-mers
Only report the k-mers that are missing
Stop after finding a value of k with missing k-mers
Search both strands of the sequence
The output of your program should find 52 missing k-mers in the E.coli genome at k=8."""
import sys
import mcb185
import itertools

def find_missing_kmers(seq):
    for k in range (1, len(seq)):
        kcount = {}
        kmer_dict = {}
        for i in range(len(seq) - k + 1):
            kmer = seq[i: i+k]
            if kmer not in kcount: kcount[kmer] = 0
            kcount[kmer] += 1
        #kmer_dict[k] = kcount
        #{k:[kmer:count, kmer:count, ...]}
        if len(kcount) != 4**k:
            missing_kmer_count = 0
            missing_kmers = []
            all_kmers = []
            for nts in itertools.product('ACGT', repeat = k):
                kmer = ''.join(nts)
                kmer = str(kmer)
                all_kmers.append(kmer)
            for possible_kmers in all_kmers:
                if possible_kmers not in kcount.keys(): 
                    missing_kmers.append(possible_kmers)
                    missing_kmer_count+=1
            if missing_kmer_count !=0 :print(f'There are {missing_kmer_count} kmers for k_mer of length {k} and they are {missing_kmers}')
            break

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    find_missing_kmers(seq)
    print("for sense strand")
    find_missing_kmers(mcb185.anti_seq(seq))
    print('for antisense starnd')
#count the number of vlaues if zero initiate the other function





