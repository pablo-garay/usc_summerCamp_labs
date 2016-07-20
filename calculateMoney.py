print("Welcome to the money counter.")

pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))
halfdollars = int(input("How many half-dollar coins do you have? "))

dollars_1 = int(input("How many $1 bills do you have? "))
dollars_5 = int(input("How many $5 bills do you have? "))
dollars_10 = int(input("How many $10 bills do you have? "))
dollars_20 = int(input("How many $20 bills do you have? "))
dollars_50 = int(input("How many $50 bills do you have? "))
dollars_100 = int(input("How many $100 bills do you have? "))

# it's better to multiply to integers and then divide rather than use floating point numbers -> efficiency
print( "You have $%.2f in your jar."
      %((pennies + nickels * 5 + dimes * 10 + quarters * 25 + halfdollars * 50 +
        100 * (dollars_1 + dollars_5 * 5 +  dollars_10 * 10 + dollars_20 * 20 + dollars_50 * 50 + dollars_100 * 100)
        ) / 100) )