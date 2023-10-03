number = input("Enter the last four digits of the number: ")

if number[0] == 8 or 9:
        if number[3] == 8 or 9:
                if number[2] == number[1]:
                        print('Telemarketer! Ignore.')
                else: 
                        print('Not a telemarketer.')
        else:
                print('Not a telemarketer.')
else:
        print('Not a telemarketer.')