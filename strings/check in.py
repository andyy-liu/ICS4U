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
            print(i)
    return 

lst = [16, 20, 4, 6]
print(true_int(lst))