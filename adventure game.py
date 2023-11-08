import time

def intro():
    print("Welcome to the Medieval Fantasy Adventure Game!")
    print("You are a brave knight on a quest to save the kingdom from a fearsome dragon.")
    print("You find yourself at a crossroads. You can go left or right.")
    choice = input("Which path will you choose? (left/right): ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid input. Please choose 'left' or 'right'.")
        intro()

def left_path():
    print("You follow the left path and encounter a group of goblins.")
    print("You can fight them, try to negotiate, or bribe them with gold.")
    choice = input("What will you do? (fight/negotiate/bribe): ").lower()
    if choice == "fight":
        print("You bravely fight the goblins and emerge victorious.")
        print("You continue your journey.")
        continue_journey()
    elif choice == "negotiate":
        print("You try to negotiate with the goblins, but they demand a valuable item in return.")
        item_choice = input("Do you have a valuable item to offer them? (yes/no): ").lower()
        if item_choice == "yes":
            print("You hand over the item and they let you pass.")
            continue_journey()
        else:
            print("You couldn't negotiate, and they attack you. You barely escape.")
    elif choice == "bribe":
        print("You offer the goblins gold, and they let you pass.")
        continue_journey()
    else:
        print("Invalid input. Please choose 'fight', 'negotiate', or 'bribe'.")
        left_path()

def right_path():
    print("You take the right path and find a mysterious cave.")
    print("You can enter the cave or avoid it.")
    choice = input("What will you do? (enter/avoid): ").lower()
    if choice == "enter":
        print("You enter the dark cave and discover a treasure chest guarded by a friendly dragon.")
        print("You share a meal with the dragon and gain its assistance on your quest.")
        continue_journey()
    elif choice == "avoid":
        print("You decide to avoid the cave and continue your quest.")
        print("You hear a distant roar.")
        continue_journey()
    else:
        print("Invalid input. Please choose 'enter' or 'avoid'.")
        right_path()

def continue_journey():
    print("You continue your journey through the dense forest.")
    print("You encounter a fork in the road. Will you go left or right?")
    choice = input("Which path will you choose? (left/right): ").lower()
    if choice == "left":
        print("You take the left path, and you come across a mystical well.")
        print("You can drink from the well or continue.")
        well_choice = input("What will you do? (drink/continue): ").lower()
        if well_choice == "drink":
            print("Drinking from the well grants you renewed strength for your quest.")
            print("You continue on your journey.")
            continue_journey()
        elif well_choice == "continue":
            print("You decide to continue without drinking from the well.")
            print("You hear a strange sound in the distance.")
            continue_journey()
        else:
            print("Invalid input. Please choose 'drink' or 'continue'.")
            continue_journey()
    elif choice == "right":
        print("You take the right path and stumble upon a hidden village.")
        print("You can rest in the village or keep moving.")
        village_choice = input("What will you do? (rest/keep moving): ").lower()
        if village_choice == "rest":
            print("You rest in the village, and the villagers offer you valuable information about the dragon's lair.")
            print("You continue your quest with newfound knowledge.")
            dragon_encounter()
        elif village_choice == "keep moving":
            print("You decide to keep moving, leaving the village behind.")
            print("You hear a faint rumble in the distance.")
            continue_journey()
        else:
            print("Invalid input. Please choose 'rest' or 'keep moving'.")
            continue_journey()

def dragon_encounter():
    print("You follow the path to the dragon's lair.")
    print("You see the fearsome dragon guarding a treasure chest.")
    print("You can choose to fight the dragon or try to negotiate with it.")
    choice = input("What will you do? (fight/negotiate): ").lower()
    if choice == "fight":
        print("You draw your sword and engage in a fierce battle with the dragon.")
        time.sleep(3)  # Simulate the battle with a delay
        print("After a long and grueling battle, you defeat the dragon!")
        print("The treasure chest is now yours.")
        print("Congratulations, you have won the treasure and saved the kingdom!")
    elif choice == "negotiate":
        print("You attempt to negotiate with the dragon.")
        print("The dragon agrees to give you the treasure in exchange for a promise to protect the kingdom.")
        print("You agree, and the dragon lets you take the treasure.")
        print("You've made a pact with the dragon and saved the kingdom!")
    else:
        print("Invalid input. Please choose 'fight' or 'negotiate'.")
        dragon_encounter()

# Start the game
intro()
