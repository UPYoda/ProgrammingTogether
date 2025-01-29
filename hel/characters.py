import random

#main player characters
character = {
    "thor": {"name": "Thor", "attack": 5, "defense": 5},
    "loki": {"name": "Loki", "attack": 3, "defense": 7},
    "odin": {"name": "Odin", "attack": 6, "defense": 4},
    "tyr": {"name": "Tyr", "attack": 2, "defense": 8}

    }

#items
items = {
    "offensive": {
        "common": {"dagger": 1, "shortsword": 2}, 
        "rare": {"axe": 3, "longsword": 3},
        "epic": {"gungnir": 4, "mjolnir": 4}
        },
    "defensive": {
        "common": {"robe": 1, "cloth helmet": 2}, 
        "rare": {"iron chestplate": 3, "iron leggings": 3},
        "epic": {"iron grippers": 4, "gleipnir": 4}
        },
   
}



#array with enemy names
enemy = [
    "giant","dragon","serpent","wolf"
    ]

#generates a random enemy from list of enemy names
def enemy_generator():
    
    # the random.randint is calling a random interger and the (0,len(enemy)-1) means choose random int from 0 to lenth of enemy array -1        *so essentially index randomly at 0, 1, 2, or 3 and return the value
    gen_enemy_id = random.randint(0,len(enemy)-1)
    e_name = enemy[gen_enemy_id]#assignes the value of the array at gen_enemy_id to e_name
    
    rarity = rarity_generator()#calls rarity of first assigned item
    e_item_off_name = list(items["offensive"][rarity])[1]#list function will create a list of items in the rarity that was assigned to this and then pick the one in the second slot with the [1]. This will be the key not the value for some reason.
    e_item_off_atk = items["offensive"][rarity][e_item_off_name]#need to get the value now 

    rarity = rarity_generator()#calls rarity again to get new value for second assigned item
    e_item_def_name = list(items["defensive"][rarity])[1]#list function will create a list of items in the rarity that was assigned to this and then pick the one in the second slot with the [1]. This will be the key not the value for some reason
    e_item_def_def = items["defensive"][rarity][e_item_def_name]#need to get the value now 

    e_attk = 0 + e_item_off_atk #placeholder in  case I want to add base stats to the enemies later
    e_def = 0+ e_item_def_def #placeholder in case i want to add base stats to the enemies later

    
    print(f"As you enter the hall you encounter a {e_name} with an attack of {e_attk} and a defense of {e_def}") #may move this over to the main.py at some point. just print values right now.
def rarity_generator():
    rarity = random.randint(1,100)
    if rarity <= 100 and rarity >=95:
        return "epic"
    elif rarity < 95 and rarity >= 80:
        return "rare"
    elif rarity > 0 and rarity < 80:
        return "common"
    else:
        print("rarity generator did not work")
    
