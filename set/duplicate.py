# Write two functions. Both functions will take a single list containing immutable data types as an argument
# 1) The first function should only use list methods and list features to remove duplicates.
# 2) The second function should remove duplicates while being allowed to use set data type features

def listdupe(lst):
    result_lst = []
    for i in lst:
        if i not in result_lst:
            result_lst.append(i)
    return result_lst

def setdupe(lst):
    setlst = set(lst)
    return setlst

mylist = [1, 1, 1, 2, 3, 3, 4]
print(listdupe(mylist))
print(setdupe(mylist))