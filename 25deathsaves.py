
import random
"""
25deathsaves.py
Death saves are a little different than normal saving throws. If your health drops to 0 or below, 
you are unconscious and may die. Each time it is your turn, roll a d20 to determine if you get closer to life or fall deeper into death.
 If the number is less than 10, you record a "failure". If the number is 10 or greater, you record a "success".
   If you collect 3 failures, you "die". If you collect 3 successes, you are "stable" but unconscious.
     If you are unlucky and roll a 1, it counts as 2 failures. 
     If you're lucky and roll a 20, you gain 1 health and have "revived". Write a program that simulates death saves. 
     What is the probability one dies, stabilizes, or revives?
"""
health_score = 0
revived = 0
success = 0
stable = 0
failure = 0
die = 0
iteration = 300
for i in range(iteration):
    x = random.randint(1, 20)
    if x == 20:
        revived = revived + 1
        break
    elif x >= 10:
        success = success + 1
        if success >= 3:
            stable = stable + 1
            break
    else: 
        if x == 1:
            failure = failure + 2
        else: failure = failure + 1
        if failure >=3:
            die = die + 1
            break
print (f'probability of being revived {revived/iteration} \n probability of being stable {stable/iteration} \n probability of dying {die/iteration}')


    