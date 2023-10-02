invalid = True
while (invalid):
    initial = (input("Input a whole number: "))

    if initial.isdigit() and "." not in initial:
        initial = int(initial)
        invalid = False

        remain = initial % 2

        if remain == 0:
            print("This number is divisible by 2.")

        else:
            print("This number is not divisible by 2.")

    else:
        print("Error - must be a whole number.")
        break

