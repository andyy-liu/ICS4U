# finding a prime number knowing that prime numbers only have 2 factors (itself and 1)
'''
prime = int(input("Enter a number greater than 1: "))
factor = 1
counter = 0

for factor in range(1, prime + 1):
    if prime % factor == 0:
        counter += 1
   
if counter == 2
    print(f"{prime} is a prime number.")
else:
    print(f"{prime} is not a prime number.")
'''
# finding a prime number while knowing that prime numbers only have factors of 1 and itself
prime = int(input("Enter a number greater than 1: "))
is_prime = True

for divider in range(2, prime):
    if prime % divider == 0:
        is_prime = False
        break

if is_prime == False:
    print(f"{prime} is not a prime number.")
else:
    print(f"{prime} is a prime number.")