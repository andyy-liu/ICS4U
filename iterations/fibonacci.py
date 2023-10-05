fib = int(input("Enter a number greater or equal to 0: "))
f0 = 0
f1 = 1
fn = 0

for fib in range(2, fib + 1): # it starts at 2 as f0 (n = 0) and f1 (n = 1) are already set above
    count = 0
    
    if count != fib:
        fn = f1 + f0
        f0 = f1
        f1 = fn
        
        count += 1

print(f"The {fib} term of the fibonacci sequence is {fn}.")