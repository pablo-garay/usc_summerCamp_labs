import random

randInt = int(random.random() * 100) + 1
# print(randInt)
print("I'm thinking of a number between 1 and 100.")

user_input = int(input("Guess a number: "))

while user_input != randInt:
    if user_input > randInt:
        print("%d is too high." % user_input)
    elif user_input < randInt:
        print("%d is too low."  % user_input)
    user_input = int(input("Guess a number: "))

print("You guessed it!")