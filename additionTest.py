import random

num_problems = int(input("How many addition problems would you like? "))

total_correct = 0
total_incorrect = 0


for i in range(1, num_problems + 1):
    print("Problem %d" % i)
    num1 = int(random.random() * 11)
    num2 = int(random.random() * 11)
    user_response = int(input("%d + %d = " % (num1, num2)))

    if num1 + num2 == user_response:
        print("That is correct!")
        total_correct += 1
    else:
        print("That is incorrect.")
        total_incorrect += 1

print("Total number correct: %d" %total_correct)
print("Total number incorrect: %d" %total_incorrect)