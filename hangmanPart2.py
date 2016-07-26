print("Welcome to Hangman!")

secretWord = str(input("Enter the secret word: "))
print("Length of secret word: %d" %len(secretWord))

def isCharInString(word, ch):
    if ch in word:
        return True
    else:
        return False

user_str = str(input("Enter a letter: "))

# check if user_str is in string
if isCharInString(secretWord, user_str):
    print("%s IS in the secret word." % user_str)
else:
    print("%s is NOT in the secret word." % user_str)
