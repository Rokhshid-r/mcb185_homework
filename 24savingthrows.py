
import random

for DC in range(5, 16, 5):
        norm_success = 0
        adv_success = 0
        dis_success = 0
        for i in range(100):
            x1 = random.randint(1, 20)
            if x1 >= DC:
                norm_success = norm_success + 1
            x2 = random.randint(1, 20)
            if max(x1, x2) >= DC:
                adv_success = adv_success + 1
            if min(x1, x2)>= DC:
                dis_success = dis_success + 1
        print (f'The probability of normal success with a DC of {DC} is {norm_success/10} ')
        print (f'The probability of success with advantage with a DC of {DC} is {adv_success/10}')
        print (f'The probability of success with disadvantage with a DC of {DC} is {dis_success/10}')
        print ('\n')

