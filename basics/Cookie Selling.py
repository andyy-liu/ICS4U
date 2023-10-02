start = float(input("What is our starting budget? "))

# num_cookies = len(input("How many normal cookies sold? "))

# num_big = len(input("How many big cookies sold? "))

cookies = input("Enter a series of b's and c's for big and normal cookies respectively: ")

num_cookies = cookies.count('c')

num_big = cookies.count('b')

cProf = (1.25 - 0.5) * num_cookies

bProf = (2 - 0.75) * num_big

totalProf = cProf + bProf 

totalMoney = start + totalProf

print(f"We sold {num_cookies + num_big} cookies!")

print(f"We made ${totalProf} from the cookies!")

print(f"We have ${totalMoney}!")