import random

odds = int(input("Input a number from 1 to 20: "))

skill = random.randint(0, 20)

print(f"Your dice rolled a {skill}.")

if skill >= odds:
    print("Success!")

else:
    print("You fail.")

