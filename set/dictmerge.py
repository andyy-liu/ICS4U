def merge(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1.keys():
            dict2[k] = v
    dict1.update(dict2)
    return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge(dict1, dict2))