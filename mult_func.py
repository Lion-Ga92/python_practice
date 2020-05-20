from sys import exit


print("Welcome to our prototype of the multi branching function script")
print("to quit type quit")

def start_story():
    print("You are walkingd down a path and come up upon two tunnels, one on the left and other on the right.")
    print("From the left tunnel you can hear a bit of a wind draft.But from the right you hear a bubbling brook ")
    print("What path do you choose?")
    choice_1_tunnel = input("You can choose 'left' or 'right' please type in lower case: ")
    if choice_1_tunnel == "left":
        print("You took the left path, and walk into a wide cavern")
        print("You light up your torch but can't see far")
        continue_left1()

    elif choice_1_tunnel == "right":
        print("You took the right tunnel, and turn on your light. It is a narrow tunnel and feels moist and damp. After walking for a few minutes your step on west soil.")
        continue_right1()

    elif choice_1_tunnel == "quit":
        print("You have clossed the script")
        exit()
    else:
        print("invalid input")
        return
def continue_left1():
    print("After walking for a few minutes your light falls upon a series of stone statues. And a small lever")
    print("Do you pull the lever? ")
    choice_2_stats = input("You can input 'yes' or 'no' as an answer. Please keep it to lowercase: ")
    if choice_2_stats == "yes":
        print("You decided to pull the lever")
        print("the statues become alive, and chose to serve you as their  master")
        exit()
    elif choice_2_stats == "no":
        print("You chose no, and a giant stone falls on you")
        exit()
    else:
        print("response not valid")

def continue_right1():
    print("You continued walking down the muddy trail, and after a few minutes fall down a rapid river and drown")
    exit()

start_story()
