# Write a Python function that takes a list of words and returns a set containing all unique letters used in these words.

def unique(lst):
    unique_set = set()
    for word in lst:
        tmp = set(word)
        unique_set = unique_set | tmp
    result = sorted(unique_set)
    return result
    

mylist = ["apple", "banana", "cherry", "date"]
print(unique(mylist))