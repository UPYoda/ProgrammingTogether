#Run on startup, introduce game and take player to the main menu
def main():
    
    print("This is my game called 'Hel' named after the Norse God for the underworld!")
    initialize_player()
    main_menu()

#Make a selection to begin game, open options, or quit
def main_menu():
    print("Please type a selection from the list:")
    print("Start Game")
    print("Options")
    print("Quit")
    select = input().strip().lower()
    selection(select)


#switch statement for the main menu
def selection(select):
    match select:
        case "start game":
            start_game()
        case "options":
            options()
        case "quit":
            quit()


#function for starting the game
def start_game():
    
    name = ""
    attack = 0
    defense = 0

    print("Choose your Character!")
    print("Type the name of the character you would like to play as!")
    print("Thor, Loki, Odin, Tyr")
    char = input().strip().lower()
    name, attack, defense = character_select(char,name,attack,defense)

    if name == "":
        start_game()
    else:
        print(f"You selected {name}. Your attack is {attack} and your defense is {defense}")


#selecting a character using match (maybe I should just use a dictionary HAHA)
def character_select(char,name,attack,defense):
    match char:
        case "thor":
            while True: #infinite loop to select thor
                x = input("Confirm (Y/N) Do you want to select thor? ").strip().lower()
                if x == "y":
                    name = "Thor"
                    attack = 5
                    defense = 5
                    break
                
                elif x == 'n':
                    name = ""
                    attack = 0
                    defense = 0
                    return name, attack, defense #returns the values of name attack and defense so they can be used outside the function
                else:
                    print("Please enter Y or N")
                    
        case "loki":
            while True: #infinite loop to select thor
                x = input("Confirm (Y/N) Do you want to select Loki? ").strip().lower()
                if x == "y":
                    name = "Loki"
                    attack = 3
                    defense = 7
                    break
                
                elif x == 'n':
                    name = ""
                    attack = 0
                    defense = 0
                    return name, attack, defense
                else:
                    print("Please enter Y or N")            

        case "odin":
            while True: #infinite loop to select thor
                x = input("Confirm (Y/N) Do you want to select Odin? ").strip().lower()
                if x == "y":
                    name = "Odin"
                    attack = 6
                    defense = 4
                    break
                
                elif x == 'n':
                    name = ""
                    attack = 0
                    defense = 0
                    return name, attack, defense
                else:
                    print("Please enter Y or N")            

        case "tyr":
            while True: #infinite loop to select thor
                x = input("Confirm (Y/N) Do you want to select Tyr? ").strip().lower()
                if x == "y":
                    name = "Tyr"
                    attack = 2
                    defense = 8
                    break
                
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
    exit()

#initialize player character
def initialize_player():
    name = "o"
    attack = 0
    defense = 0
    return name, attack, defense











main()    