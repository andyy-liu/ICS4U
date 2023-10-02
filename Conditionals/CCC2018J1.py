invalid = True
number = ''

while invalid:
   number = int(input("Enter the seven digit number: "))
if len(number) == 7:
        invalid = False

lastDigits = number / 10000

if 