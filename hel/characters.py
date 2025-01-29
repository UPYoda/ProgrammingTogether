import random

#main player characters
character = {
    "thor": {"name": "Thor", "attack": 5, "defense": 5},
    "loki": {"name": "Loki", "attack": 3, "defense": 7},
    "odin": {"name": "Odin", "attack": 6, "defense": 4},
    "tyr": {"name": "Tyr", "attack": 2, "defense": 8}

    }







#array with enemy names
enemy = [
    "giant","dragon","serpent","wolf"
    ]

#generates a random enemy from list of enemy names
def enemy_generator():
    
    # the random.randint is calling a random interger and the (0,len(enemy)-1) means choose random int from 0 to lenth of enemy array -1        *so essentially index randomly at 0, 1, 2, or 3 and return the value
    print(f"As you enter the hall you encounter a {enemy[random.randint(0,len(enemy)-1)]}") 

