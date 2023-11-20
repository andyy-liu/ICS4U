def filter(dict, threshold):
    new_dict = {}
    for k, v in dict.items():
        if v >= threshold:
            new_dict[k] = v
    return new_dict


dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
print(filter(dict, 10))