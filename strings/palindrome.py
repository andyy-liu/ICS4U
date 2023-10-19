word = input('Enter a word: ')

flipped = word[::-1]

if word.startswith(word) is word.endswith(flipped):
    print('Palindrome!')
else:
    print('Not a palindrome')