print("Welcome to Hangman!")

secretWord = str(input("Enter the secret word: "))
print("Length of secret word: %d" %len(secretWord))

def isCharInString(word, ch):
    if ch.lower() in word.lower():
        return True
    else:
        return False

incorrect_guesses = 0

while(incorrect_guesses < 7):
    user_str = str(input("\nEnter a letter: "))

    # check if user_str is in string
    if isCharInString(secretWord, user_str):
        print("%s IS in the secret word." % user_str)
    else:
        print("%s is NOT in the secret word." % user_str)
        incorrect_guesses += 1
        print("That is incorrect guess #%d.\n" %incorrect_guesses)

print("Game over.")