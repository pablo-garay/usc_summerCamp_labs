print("Welcome to Hangman!")

secretWord ="hello"

def isCharInString(word, ch):
    if ch in word:
        return True
    else:
        return False

