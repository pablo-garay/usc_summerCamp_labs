print("Welcome to Hangman!")

secretWord ="hello"

def isCharInString(word, ch):
    if ch in word:
        return True
    else:
        return False

user_str = str(input("Enter a letter: "))

# check if char is in string
if isCharInString(secretWord, user_str):
    print("%s IS in the word %s." % (user_str, secretWord))
else:
    print("%s is NOT in the word %s." % (user_str, secretWord))