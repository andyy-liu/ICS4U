# Write a function that counts the number of consonants in the given string argument. The function should return an integer
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter a word: ')

count = 0
for i in word:
    if i not in vowels:
        count += 1
    
print(f"Your word has {count} consonants.")
