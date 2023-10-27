def f(x):
    if x < 1:
        return False
    else:
        count = 0
        for divider in range(1, x):
            if x % divider == 0:
                count += 1
        
        if count == 4:
            return True
        else:
            return False

def true_int(lst):
    for i in lst:
        if f(i) == True:
            return i

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(true_int(lst))