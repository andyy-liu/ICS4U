marks = input("Enter a set of marks from 1 to 100, seperated by spaces: ").split() 
sum = 0

# this converts the users input into integers
for i in range(0, len(marks)): # the reason why its len(marks) and not len(marks) + 1 is because index starts at 0
    marks[i] = int(marks[i])

for i in range(0, len(marks)):
    sum += marks[i]

average = sum / len(marks)

print(f"Your average is {average}.")