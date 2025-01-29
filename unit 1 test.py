
#1)
import math

def find_dist(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    c = math.sqrt(a**2 + b**2)
    return c

#2)
def valid_prob(prob):
    if 0 <=float(prob)<= 1:
        print("This is a valid probability")
    else:
        return None
    
#5)
def max(a, b, c, d):
    if a>=b and a>=d and a>=c: 
        return a
    elif b>=a and b>=c and b>=d:
        return b
    elif c>=a and c>=b and c>=d:
        return c
    else:
        return d

print(max(2, 3, 7, 1))