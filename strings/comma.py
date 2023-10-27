# Create a function that takes a string argument with a comma separating different integer values. Convert the argument to a list of integers.
# Example: “1,2,3,4,5” → [1,2,3,4,5]

strlist = input('Enter a list of numbers, seperated by commas: ').split(',')
numlist = [eval(i) for i in strlist]
print(numlist)