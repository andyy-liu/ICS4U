# solution 1
word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

word1 = ' '.join(word1)
word2 = ' '.join(word2)

word1 = word1.split()
word2 = word2.split()

word1 = word1.sort()
word2 = word2.sort()

if word1 == word2:
    print('Anagram!')
else:
    print('Not an anagram.')

# solution 2 (compares each letter after making the words into a list and sorting them)
def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        word1list = sorted(word1)
        word2list = sorted(word2)

        for i, character in enumerate(word1list):
            if word2list[i] != character:
                return False
        return True

# solution 3 (compares how many times each letter appears in each word)
def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
        return True
