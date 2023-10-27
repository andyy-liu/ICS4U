# Implement a function that performs basic string compression using the counts of repeated characters. Return the string if the compression is longer or the same length as the argument.
# For example, "aabcccccaaa" would become "a2b1c5a3.

def compress(mystr):
    result = ''
    counter = 1 # counter starts at 1 to represent the first appearence of the char
    for i in range(1, len(mystr)): # set range to start at 1 to ignore the first char as counter is already 1
        if mystr[i] == mystr[i - 1]: # checking if the char matches the one before
            counter += 1
        else: # if it doesn't match, concatenate
            result += mystr[i - 1] # adds the char 
            result += str(counter) # adds the frequency
            counter = 1 # resets the counter

    result += mystr[-1] + str(counter) # accounts for last char by concatenating the last char and the freq

    if len(result) < len(mystr):
        return result
    else:
        return mystr

print(compress('aabcccccaaa'))
