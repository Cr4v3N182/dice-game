import random

set = [1, 2, 3, 4, 5]
set1 = []

#player_1 shuffle
def roll_dice1():
    for el in set:
        el = random.randint(1, 6)
        set1.append(el)
    return set1

print(roll_dice1())

#player_2 shuffle
def roll_dice2():
    for el in set:
        el = random.randint(1, 6)
        set2.append(el)
    return set1

print(roll_dice2())

    
