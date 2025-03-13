import math
for i in range(1, 101):
    for j in range (1, 101):
        c = i**2 + j**2
        if math.sqrt(c)%1 == 0:
            print (i, j, math.sqrt(c))
