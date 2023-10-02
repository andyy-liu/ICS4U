import random

invalid = True
player = ''

while invalid:
    player = input("Choose between rock, paper, or scissors: ")

    if player in {'rock', 'paper', 'scissors'}:
        invalid = False

cpu = random.choice(['rock', 'paper', 'scissors'])
print(f"The CPU chose {cpu}")

if cpu == player:
    print("Tie game.")

else:
    if cpu == 'rock':   
        if player == 'paper':
            print("Player wins.")
        else:
            print("CPU wins.")

    elif cpu == 'paper':
        if player == 'scissors':
            print("Player wins.")
        else:
            print("CPU wins")
    else:
        if player == 'rock':
            print("Player wins.")
        else:
            print("CPU wins.")

    
