print("Welcome to Hangman!")

secretWord ="hello"

def isuser_strInString(word, ch):
    if ch in word:
        return True
    else:
        return False

user_str = str(input("Enter a letter: "))

# check if user_str is in string
if isuser_strInString(secretWord, user_str):
    print("%s IS in the secret word." % user_str)
else:
    print("%s is NOT in the secret word." % user_str)
