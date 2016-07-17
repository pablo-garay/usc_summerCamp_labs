total = 0

while True:
    print("""
    p) Pennies
    n) Nickels
    d) Dimes
    q) Quarters
    h) Half-Dollars
    $) Dollar Coins
    x) No more coins
    """)
    type = input("Which coins do you have in your pocket (p, n, d, q, h, $)? ")

    if type not in ["p", "n", "d", "q", "h", "$"]:
        break

    if type == "p":
        denomination = "pennies"
    elif type == "n":
        denomination = "nickels"
    elif type == "d":
        denomination = "dimes"
    elif type == "q":
        denomination = "quarters"
    elif type == "h":
        denomination = "half-dollars"
    elif type == "$":
        denomination = "dollars"

    num = int(input("Number of " + denomination + ": "))

    if type == "p":
        total += num
    elif type == "n":
        total += num * 5
    elif type == "d":
        total += num * 10
    elif type == "q":
        total += num * 25
    elif type == "h":
        total += num * 50
    elif type == "$":
        total += num * 100

    print("You have %d cents in your pocket." %total)

