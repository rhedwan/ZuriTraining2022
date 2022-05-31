import random

print("""
[Rock-Paper-Scissors] CLI Game

    "R" for "rock", 
    "P" for "paper", 
    "S" for "scissors".
    
""")

def value_checker(value):
    if value == "r":
        return "rock"
    elif value == "p":
        return "paper"
    elif value == "s":
        return "scissors"

values = ["r","p" ,"s"]
isValid = True
isPlaying = True
while isPlaying:
    while isValid:
        player = input(f"Player, make your move: ").lower()

        if player not in values :
            print("\nInvalid Entry")
            isValid = True
            continue
        break
    
    computer = random.choice(values)
    action_computer = value_checker(computer)
    action_player = value_checker(player)
    print(f"You Played '{ action_player}'")
    print(f"Computer Played '{action_computer}' \n")

    if player == computer:
        print("It's a tie!")
        isPlaying = True

    elif player == "r":
        if computer == "s":
            print("Player wins! 🎊")
        else:
            print("Computer wins! 💻")
        isPlaying = False


    elif player == "p":
        if computer == "r":
            print("Player wins! 🎊")
        else:
            print("Computer wins! 💻")
        isPlaying = False


    elif player == "s":
        if computer == "p":
            print("Player wins! 🎊")
        else:
            print("Computer wins! 💻")
        isPlaying = False
