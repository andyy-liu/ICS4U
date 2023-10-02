import math

fences = int(len(input("Input the amount of fences: ")))

cansReq = math.ceil(fences / 12)

cansActual = cansReq * 12

cansLeft = cansActual - fences

cansCost = round(cansReq * 14.95,2)

print(cansActual)
print(cansLeft)
print(cansCost)