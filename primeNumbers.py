from math import sqrt

is_prime = True
number = int(input("Enter a number: "))

for i in range(2, int(sqrt(number)) + 1):
    if number % i == 0:
        print("%d is a composite number.\nThe smallest integer greater than 1 that divides it evenly is %d." %(number, i))
        is_prime = False

if is_prime == True:
    print("%d is a prime number." %number)