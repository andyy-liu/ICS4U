# Write a Python function that takes a list of sets and returns the count of elements that are common to all the sets.

def intersect(a, b, c):
    ''' 
    finds the number of matching elemnents in all sets
    takes multiple sets of numbers
    returns the number of matching elements as an integer
    '''
    result = a & b & c
    count = len(result)
    return count

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}
print(intersect(set1, set2, set3))