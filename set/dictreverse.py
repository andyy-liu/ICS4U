def reverse(dict):
    flip_dict = {v: k for k, v in dict.items()} # applies v: k for all key-value pairs in dict.items
    return flip_dict

dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse(dict))