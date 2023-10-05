# solution using for loops

'''product = 1
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    product *= i # multiplies the variable by the index number then assigns the product back into the variable
print(f'The factorial of {num} is {product}.')'''

# solution using while loops
end_result = 1
product = 1
num = int(input("Enter a number: "))

while product <= num: 
    end_result *= product 
    product += 1

print(f'The factorial of {num} is {end_result}.')