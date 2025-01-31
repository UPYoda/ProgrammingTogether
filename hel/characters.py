import random
import csv


#main player characters
character = {
    "thor": {"name": "Thor", "attack": 5, "defense": 5},
    "loki": {"name": "Loki", "attack": 3, "defense": 7},
    "odin": {"name": "Odin", "attack": 6, "defense": 4},
    "tyr": {"name": "Tyr", "attack": 2, "defense": 8}

    }



items = {}

# Read the CSV file
with open("items.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile) #read csv file as a dictionary
    
    for row in reader:
        category = row["Type"].lower()
        rarity = row["Rarity"].lower()
        item_name = row["Item"]
        power = int(row["Power"])

        # Initialize categories if not exists
        if category not in items:
            items[category] = {}

        if rarity not in items[category]:
            items[category][rarity] = {}

        # Add the item to the corresponding place
        items[category][rarity][item_name] = power


class Enemy: #NOT YET USED
    def __init__(self, inventory):
        self.inventory = inventory







troll = Enemy(inventory=items)
#print(Enemy.inventory)















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
    e_item_off_name = list(items["offensive"][rarity])[random.randint(0,len(items["offensive"][rarity])-1)]#list function will create a list of items in the rarity that was assigned to this and then pick the one in a random slot. This will be the key not the value because we are choosing from a list
    e_item_off_atk = items["offensive"][rarity][e_item_off_name]#need to get the value now 

    rarity = rarity_generator()#calls rarity again to get new value for second assigned item
    e_item_def_name = list(items["defensive"][rarity])[random.randint(0,len(items["defensive"][rarity])-1)]#list function will create a list of items in the rarity that was assigned to this and then pick the one in a random slot. This will be the key not the value becasue we are choosing from a list
    e_item_def_def = items["defensive"][rarity][e_item_def_name]#need to get the value now 

    e_attk = 0 + e_item_off_atk #placeholder in  case I want to add base stats to the enemies later
    e_def = 0+ e_item_def_def #placeholder in case i want to add base stats to the enemies later

    #store enemy values in an array that we can import to the main fuction? (idk if this will be useful or not) **creates a dict with enemy name [key(off name):value(off atk), key(def name):value(def def)]
    e1 = {
        e_name : { e_item_off_name : e_item_off_atk, 
                  e_item_def_name : e_item_def_def
                }
    }
    
    print(f"As you enter the hall you encounter a {e_name} weilding a {e_item_off_name} with an attack of {e_attk} and wearing the {e_item_def_name} with a defense of {e_def}\n") #may move this over to the main.py at some point. just print values right now.

    return e1 #returns a now fully randomly generated enemy, which im not using yet anywhere I just thought it might be useful later




#returns an item type for the rarity
def rarity_generator():
    rarity = random.randint(1,100)
    if rarity <= 100 and rarity > 98:
        return "legendary"
    elif rarity <= 98 and rarity >= 95:
        return "epic"
    elif rarity < 95 and rarity >= 80:
        return "rare"
    elif rarity > 0 and rarity < 80:
        return "common"
    else:
        print("rarity generator did not work")
    




    



