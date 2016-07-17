print("Welcome to the palindrome program.")
word = input("Enter a word: ")

def isPalindrome(str):
    i = 0
    j = len(word) - 1

    while i < j:
        if (word[i] != word[j]):
            return False
        i += 1
        j -= 1
    return True


if isPalindrome(word):
    print("%s IS a palindrome." %word)
else:
    print("%s is not a palindrome." %word)