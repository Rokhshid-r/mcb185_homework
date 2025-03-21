
#import mcb185
#import sys
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
seq = "ATGCGTTGTACGTAGACGTGCATTGATGCTAGGCAGTATGCGGCATTGTAATGAAAAGCACGTAAAUGGGGCGCCGCTTATGTAGTAG"

def translate(dna, x):    
    aas = []
    if x >= 0:
        dna = dna[::1]
    else: dna = dna[::-1]; x = x*-1
    for i in range(x-1, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            if   codon == 'ATG': aas.append('M')
            elif codon == 'TAA': aas.append('*')
            elif codon == 'TAG': aas.append('*')
            elif codon == 'TGA': aas.append('*')
            else:                aas.append('X')
    aa_seq = ''.join(aas)
    print (aa_seq)
    return aa_seq

def find_orf(aa_seq):
    pre_pos = 0
    orf_list = []
    for pos, letter in enumerate(aa_seq):
        if letter == '*':
            segment = aa_seq[pre_pos:pos + 1]
            pre_pos = pos
            for start_pos, letter in enumerate(segment):
                if letter == 'M':
                    orf = segment[start_pos:]
                    if len(orf)> protein_length:
                        orf_list.append(orf)
    print (orf_list)


find_orf(translate(seq, 3))
    
         
"""




def forward_frames(seq, x):

    codon_list = []
    for i in range(x, len(seq), 3):
        codon = seq[i:i+3]
        codon_list.append(codon)
    for codon, pos in enumerate(codon_list):
        if codon in start_codon:
            for codon, stop_pos in enumerate(codon_list[pos:]):
                if codon in stop_codons:
                    pass
                    































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

"""