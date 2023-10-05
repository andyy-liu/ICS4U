perfect = 0

for num in range(1, 10000):

    sum = 0
    for factor in range(1, num + 1):
        if num % factor == 0:
            sum += factor
       
    if sum == num:
        perfect += num
        print(f"{num} is a perfect number.")

print(f"The total sum of all perfect numbers under 10001 is {perfect}.")
    


