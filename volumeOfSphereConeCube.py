pi = 3.14159265

print("Enter 1 to find area of sphere. Enter 2 to find area of cone. Enter 3 to find area of cube.")

user_input = float(input("Your selection: "))
items = [1, 2, 3]

if user_input in items:

    if user_input == 1:
        radius = float(input("Enter radius for sphere: "))
        print("The volume of the sphere with radius %f is %f." %( radius, (4/3) * pi * radius ** 3) )

    elif user_input == 2:
        radius = float(input("Enter radius for cone: "))
        height = float(input("Enter height for cone: "))
        print("The volume of the cone with radius %f and height %f is %f."
              %(radius, height, radius ** 2 * pi * height / 3))

    else:
        side = float(input("Enter side length for cube: "))
        print("The volume of the cube with side of %f is %f." %(side, side ** 3))

else:
    print("Uh oh, I don't know about that item")