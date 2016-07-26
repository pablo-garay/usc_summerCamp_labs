def isCharInString(word, ch):
    if ch in word:
        return True
    else:
        return False


run = "yes"

while run == "yes":
    # user input
    word = str(input("Enter a word: "))
    char = str(input("Enter a character: "))

    # check if char is in string
    if isCharInString(word, char):
        print("%s IS in the word %s." %(char, word))
    else:
        print("%s is NOT in the word %s." % (char, word))

    #ask if should run again
    run = str(input("\nWould you like to try another word? ")).lower()

    # validate user input
    while(run not in ("yes", "no")):
        print("N is not a valid answer to the question.")
        run = str(input("Would you like to try another word? ")).lower()

print("Thank you for using my program.")