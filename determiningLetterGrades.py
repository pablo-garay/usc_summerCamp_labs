percentage = int(input("Enter a percentage: "))
indefinite_article = "a"

if percentage == 0:
    letter_grade = "F"
    indefinite_article = "an"
elif percentage < 60:
    letter_grade = "E"
    indefinite_article = "an"
elif percentage < 70:
    letter_grade = "D"
elif percentage < 80:
    letter_grade = "C"
elif percentage < 90:
    letter_grade = "B"
elif percentage >= 90:
    letter_grade = "A"
    indefinite_article = "an"

print("%d%% is %s %s." %(percentage, indefinite_article, letter_grade))