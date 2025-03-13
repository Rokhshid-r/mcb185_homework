
import math
import sys
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
min = 255**3
with open(colorfile, 'r') as file:
    for line in file:
        list = line.split()
        color_cord = list[2].split(',')
        red = int(color_cord[0])
        green = int(color_cord[1])
        blue = int(color_cord[2])
        distance = math.sqrt((blue - B)**2 + (red - R)**2 + (green - G)**2)
        if distance <= min: min = distance; color = list[0]
print(color)

    


    


