


import sys
import random
import math
alphabet = 'ACGT' #sys.argv[1]
match = '+1' #sys.argv[2]
mismatch = '-1' #sys.argv[3]
nt_list = list(alphabet)
print('   ', end='')
for i in alphabet:
    print (i, end='  ') 


for j in alphabet:
        print (f"\n{j}", end=' ')
        for i in range (0, len(nt_list)):
            if nt_list[i] == j:
                print (match, end = ' ')
            else:
                print(mismatch, end = ' ')
            