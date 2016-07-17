pi = 3.14159265

print("Enter 1 to find area of circle. Enter 2 to find area of rectangle")

user_input = float(input("Your selection: "))
items = [1, 2]

if user_input in items:
    print("Found element in list!")
    print(pi)

    if user_input == 1:
        radius = float(input("Enter radius for circle: "))
        print("The circle with radius of %f has an area of %.8f." % (radius, pi * radius ** 2))

    else:
        side1 = float(input("Enter length for side 1 of rectangle: "))
        side2 = float(input("Enter length for side 2 of rectangle: "))
        print("The rectangle with length %f and width %f has an area of %f." % (side1, side2, side1 * side2))

else:
    print("Uh oh, I don't know about that item")
