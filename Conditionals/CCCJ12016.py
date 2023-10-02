win_counter = 0 
for i in range (6):
    current_result = input(f"Enter the result of game {i+1}: ")

    if current_result == "W" or "w":
        win_counter += 1

group = 0 
if win_counter > 4:
    group = 1
elif win_counter > 2:
    group = 2
elif win_counter > 0:
    group = 3

if group == 0:
    print("You are eliminated.")

else:
    print(f"You are placed in group {group}!")

