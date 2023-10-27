# Create a function that removes duplicates from the given list argument.
# Example: [“a”,”b”, ”c”, “c”, “b”, “c”, “a”, “a”, “d”] → [“a”, “b”, “c”, “d”]

def remove(lst):
    result_list = []
    lst.sort()
    for i in lst:
        if i not in result_list:
            result_list += i
    return result_list

lst = ["a","b", "c", "c", "b", "c", "a", "a", "d"]
print(remove(lst))