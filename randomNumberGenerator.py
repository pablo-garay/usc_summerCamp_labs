import random

def getRandomValue(min, max):
    return int(random.random() * (max - min) + min)

min = int(input("Enter a minimum value: "))
max = int(input("Enter a maximum value: "))

if min > max:
    print("The maximum value has to be greater than the minimum value")
    exit(1)

print("Here are 10 random numbers between %d and %d: " %(min, max))
for i in range(9):
    print("%d, " %getRandomValue(min, max), end="")
print("%d" %getRandomValue(min, max))
