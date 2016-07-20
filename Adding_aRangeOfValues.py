num1 = int(input("Enter the lower value: "))
num2 = int(input("Enter the higher value: "))

while num1 >= num2:
    print("The lower value is not less than the higher value.")
    num1 = int(input("Enter the lower value: "))
    num2 = int(input("Enter the higher value: "))

total = 0

for i in range(num1, num2 + 1):
    total += i

print("The sum from %d to %d is %d." %(num1, num2, total))