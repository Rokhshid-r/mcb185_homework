
"""The number of values
The minimum and maximum values
The mean and standard deviation
The median value"""
import sys
import math

numbers = []
input_list = sys.argv[1:]
for arg in input_list:
    numbers.append(float(arg))

max = numbers[0]
min = numbers[0]
sum = 0
values = len(numbers)
for number in numbers:
    sum += number
    if number > max: max = number
    if number < min: min = number 
mean = sum/values
sd_num = 0
for number in numbers:
    sd_num += (number - mean)**2
sd = math.sqrt(sd_num/values)

print(f'The min is {min}')
print(f'The max is {max}')
print(f'SD is {sd}')
print(f'The means is {mean}')