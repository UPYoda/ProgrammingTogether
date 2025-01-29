import random

enemy = [
    "giant","dragon","serpent","wolf"
    ]


def enemy_generator():
    print(f"As you enter the hall you encounter a {enemy[random.randint(0,len(enemy))]}")
