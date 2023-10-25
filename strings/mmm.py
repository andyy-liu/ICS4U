strlist = input('Enter a list of numbers seperated by a space: ').split()
numlist = [eval(i) for i in strlist]

avg = 0
def mean(numlist):
    total = 0
    for i in numlist:
        total += i
    avg = total / len(numlist)
    return avg

sortlist = []
def median(numlist):
    sortlist = sorted(numlist)
    lenlist = len(numlist)
    i = (lenlist - 1) // 2

    if (lenlist % 2):
        return sortlist[i]
    else:
        return sortlist[i] + sortlist[i + 1] / 2.0

def mode(numlist):
    # have to find a way to account for no mode
    maxmode = max(set(numlist), key = numlist.count)

    return maxmode

print(f'Mean is {mean(numlist)}')
print(f'Median is {median(numlist)}')
print(f'Mode is {mode(numlist)}')