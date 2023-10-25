strlist = input('Enter a list of numbers, seperated by commas: ').split(',')
numlist = [eval(i) for i in strlist]
print(numlist)