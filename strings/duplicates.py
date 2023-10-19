word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

match = [] 
def duplicate(word1, word2): 
    for i in word1:
        if i in word2:
            match.append(i)
    return sorted(match)

print(duplicate(word1, word2))