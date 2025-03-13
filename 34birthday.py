

import sys
import random
import math
trials = 100 #int(sys.argv[1])
days = 365 #int(sys.argv[2])
people = 23 #int(sys.argv[3])
shared = 0
for trial in range(0, trials):
    same_day = False
    calender = [0]*365
    for i in range(0, people):
        birthday = random.randint(0, days - 1)
        calender[birthday] += 1
        if calender[birthday] > 1:
            same_day = True
            break
    if same_day is True:
        shared += 1
print (shared/trials)




