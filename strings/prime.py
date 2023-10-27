# Create a function that returns True if the given integer argument is a prime number.

def prime(num):
    counter = 0
    for i in range(2, num):
        if num % i == 0:
            counter += 1
    if counter != 0:
        return False
    else:
        return True

print(prime(4))
