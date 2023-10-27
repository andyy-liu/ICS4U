# Create a function that returns a list of factors of the integer argument

def factor(num):
    numlist = []
    for divider in range(1, num + 1):
        if num % divider == 0:
            numlist.append(divider)
    return numlist

print(factor(12))