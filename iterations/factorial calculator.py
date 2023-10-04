'''
product = 1
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    product *= i
print(f'The factorial of {num} is {product}.')
'''

end_result = 1
product = 1
num = int(input("Enter a number: "))
while product <= num:
    end_result *= product
    product = product + 1

print(f'The factorial of {num} is {end_result}.')