
#import mcb185
import sys
"""
Write a program that finds open reading frames in the E. coli genome.

Input: multi-FASTA file of DNA
Output: multi-FASTA file of proteins
Must perform a six-frame translation
Proteins must be at least 100 amino acids long
Proteins must start with 'M' and end with '*'
Deflines must have unique identifiers"""
stop_codons = ['TAA','TAG','TGA']
start_codon = 'ATG'
#file = sys.argv[1]
protein_length = 1
#for defline, seq in mcb185.read_fasta(file):
#    sequence = seq
seq = 'ACGTGCATTGATGCTAGGCAGT'
def positive_frame_tr(seq, x):
    frame_1 = []
    for i in range(x, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3: frame_1.append(codon)
    stop_codon_pos = []
    for pos, codon in enumerate(frame_1):
        if codon in stop_codons:
            stop_codon_pos.append((pos + 1)*3)
    segments = []
    for pos in stop_codon_pos:
        segment = seq[x:pos]
        if len(segment) > protein_length*3:
            segments.append([segment, pos, x])
            print(segments)

    print (f'Stop codon positions for reading fram {x} are {(stop_codon_pos)}')
    #return stop_codon_pos
            
    print(stop_codon_pos)
    print(frame_1)
positive_frame_tr(seq, 2)

