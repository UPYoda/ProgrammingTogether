import random

#array with enemy names
enemy = [
    "giant","dragon","serpent","wolf"
    ]

#generates a random enemy from list of enemy names
def enemy_generator():
    print(f"As you enter the hall you encounter a {enemy[random.randint(0,len(enemy)-1)]}") # the random.randint is calling a random interger and the (0,len(enemy)-1) means choose random int from 0 to lenth of enemy array -1 *so essentially index randomly at 0,1,2,3
