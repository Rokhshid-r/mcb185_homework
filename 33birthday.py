

import sys
import random
import math
trials = 10000 #int(sys.argv[1])
days = 365 #int(sys.argv[2])
people = 23 #int(sys.argv[3])
shared = 0

for trial in range(0, trials):
    birthday_list = []
    for i in range(0, people):
        day = random.randint(0, 365)
        birthday_list.append(day)
    same_day = False
    for i in range(0, len(birthday_list)):
        for j in range(i + 1, len(birthday_list)):
            if birthday_list[i] == birthday_list[j]:
                same_day = True
                break
    if same_day is True: 
        shared += 1

print(shared/trials)

            