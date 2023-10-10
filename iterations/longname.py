namelist = []
name = ''
while name != "X":
    name = input("Enter a name: ")
    
    if name != 'X': # adds the names into a list
        namelist.append(name)
        max_len = 0

    for i in namelist: # indexes the list to find the term with the most amount of characters
        if len(i) > max_len: 
            max_len = len(i) # sets the number of characters to max_len
            max_name = i 

print(f'The longest name with {max_len} characters is {max_name}.')

'''name = ''
max_len = 0
max_name = ''

while name != 'X':
    name = input("Enter a name: ")

    if name != 'X':
        current_len = len(name)

        if current_len > max_len:
            max_len = current_len
            max_name = name
    else:
        print('End of loop.')

if max_name:
    print(f'The longest name with {max_len} characters is {max_name}.')
else:
    print('Not enough info.')'''
