import random

set = [1, 2, 3, 4, 5]
p1_list = []
p2_list = []

#player_1 shuffle
def roll_dice1():
    for el in set:
        el = random.randint(1, 6)
        p1_list.append(el)
    return p1_list

#print(roll_dice1())

#player_2 shuffle
def roll_dice2():
    for el in set:
        el = random.randint(1, 6)
        p2_list.append(el)
    return p2_list

#print(roll_dice2())

    
