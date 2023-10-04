num = int(input("Enter a number greater than 0: "))
factor = 1

for factor in range(1, num + 1):
    if num % factor == 0:
        print(factor)