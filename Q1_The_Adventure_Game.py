#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
            pass
elif place == "cave":
    light = input("light a torch or proceed in the dark ")
    if light == "light a torch":
        print("You found treasure!!")
    elif light == "proceed in the dark":
        print("You got lost in the cave Forever :(")
    else:
         pass
    
