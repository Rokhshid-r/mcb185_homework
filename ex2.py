
import random
for i in range(100):
    above = 0
    below = 0
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    if b >= a**2:
        above = above + 1
    else:
        below = below + 1
pi = above/(above + below)
print (pi)


