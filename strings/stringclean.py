word = input('Enter an word: ').replace(' ', '').lower()

for i in '0123456789':
    word = word.replace(i, '')  

print(word)