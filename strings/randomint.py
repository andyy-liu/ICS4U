# Create a function that takes 3 arguments: (start, end, frequency). The function should return a list of random [frequency] many integers from [start, end].
import random

def f(x, y, z):
    for i in range(z):
        print(random.randint(x, y))
    return

f(0, 9, 10)