print("Chinese Zodiak")
year = int(input("Enter year: "))

zodiak = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
print("%d is the Year of the %s." %(year, zodiak[year % 12]))