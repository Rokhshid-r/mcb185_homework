

import sys
import math
prob = []
for arg in sys.argv[1:]:
    f = float(arg)
    if f >= 1 and f <=0: sys.exit('not a probability')
    prob.append(f)

total = 0
for p in prob:
    total += p
if not math.isclose(total, 1.0):
    sys.exit('error, does not sum up to 1')

h = 0
for p in prob:
    h -= p*math.log2(p)
print(f'{h:.4f}')


