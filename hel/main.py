from characters import character

#Run on startup, introduce game and take player to the main menu
def main():
    
    print("This is my game called 'Hel' named after the Norse God for the underworld!")
    main_menu()

#Make a selection to begin game, open options, or quit
def main_menu():
    print("Please type a selection from the list:")
    print("Start Game")
    print("Options")
    print("Quit")
    select = input().strip().lower()

    #match statement to choose what the user inputs
    match select:
        case "start game":
            start_game()
        case "options":
            options()
        case "quit":
            quit()
        case _:
            print("Invalid selection.")


#function for starting the game
def start_game():
    
    #initialize player values
    name = ""
    attack = 0
    defense = 0

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
        return name, attack, defense








#function for opening options menu
def options():
    print("Options")

#function for quitting game
def quit():
    print("Thanks for playing!")
    exit()












main()    