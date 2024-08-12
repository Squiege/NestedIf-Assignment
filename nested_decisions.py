# Task 1
#Task 3 is incorporated with Task 1 and 2. Adding pass statements

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
    print("You find a hidden treasure!")

#Task 2

    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You burn your hand!")
    elif action == "proceed in the dark":
        print("You cant see a thing!")
    else:
        pass
else:
    pass


