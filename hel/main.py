from characters import character
from enemies import enemy_generator


#Run on startup, introduce game and take player to the main menu
def main():
    
    print("This is my game called 'Hel' named after the Norse God for the underworld!")
    while True:
        select = main_menu()
        selection(select)
        room_generator()
        break


#Make a selection to begin game, open options, or quit
def main_menu():
    
    while True:
        print("Please type a selection from the list:")
        print("Start Game")
        print("Options")
        print("Quit")
        select = input().strip().lower()
        if select not in ["start game", "options", "quit"]: #ensure that the user inputs one of the menu options
            print("Invalid Selection")
        else:
            return select


#switch statement for the main menu
def selection(select):
    while True:
        if select == "start game":
            return start_game()
        elif select == "options":
            return options()
        elif select == "quit":
            return quit()
        else:
            print("Invalid selection.")


#function for starting the game
def start_game():
    
    #Character selection
    name, attack, defense = char_select()

    #check to ensure character was selected and display stats
    if name == "":
        start_game()
    else:
        print(f"You selected {name}. Your attack is {attack} and your defense is {defense}")
        



#selecting a character
def char_select():
    print("Choose your Character!")
    print("Type the name of the character you would like to play as!")
    print("Thor, Loki, Odin, Tyr")
    char = input().strip().lower()

    while True:
        x = input(f"Confirm (Y/N) Do you want to select {character[char]["name"]}? ").strip().lower() #look into characters dictionary list
        if x == "y":
            name = char
            attack = character[char]["attack"]
            defense = character[char]["defense"]
            return name, attack, defense
        elif x == 'n':
            name = ""
            attack = 0
            defense = 0
            return name, attack, defense
        else:
            print("Please enter Y or N")



def room_generator():
    print("You enter the room")
    enemy_generator()
    while True:
        x = input("Would you like to go left or right? ").strip().lower()
        if x == "left":
            print("You go left.")
            return False
        elif x == "right":
            print("You go right.")
            return False
        else:
            print("Invalid response")





#function for opening options menu
def options():
    print("Options")
    exit() #placeholder until we add loop or something to add options or bring user back to menu

#function for quitting game
def quit():
    print("Thanks for playing!")
    exit()












main()    