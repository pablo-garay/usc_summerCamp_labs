print("Welcome to Hangman!")

secretWord = str(input("Enter the secret word: "))
secretWordLength = len(secretWord)
print("Length of secret word: %d" %secretWordLength)

def isCharInString(word, ch):
    if ch.lower() in word.lower():
        return True
    else:
        return False

incorrect_guesses = 0
correct_guesses = 0

while(incorrect_guesses < 7 and correct_guesses < secretWordLength):
    user_str = str(input("\nEnter a letter: "))

    # check if user_str is in string
    if isCharInString(secretWord, user_str):
        print("%s IS in the secret word at index %d." % (user_str, secretWord.find(user_str)))
        correct_guesses += len(user_str)
        #remove guessed char from string
        secretWord = secretWord.replace(user_str, "")

    else:
        print("%s is NOT in the secret word." % user_str)
        incorrect_guesses += 1
        print("That is incorrect guess #%d.\n" %incorrect_guesses)

if correct_guesses == secretWordLength:
    print("You guessed the word! You win! Congratulations!")
else:
    print("Game over.")