upper = int(input("Enter a number greater than 1: "))
result_num = 0
max_count = 0

for num in range(1, upper + 1):
    counter = 0
    
    for factor in range(1, num + 1):
        if num % factor == 0:
            counter += 1

    if counter > max_count:
        max_count = counter
        result_num = num

print(f"The number {result_num} has the most factors with {max_count} factors.")