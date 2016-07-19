from sys import argv

if (len(argv) != 3):
    print("Usage: Include two command line parameters x and y to find x^y")
    exit(1)

print("Program that raises x to y i.e. it finds x^y")
x = float(argv[1])
y = float(argv[2])

print("%f^%f = %f" %(x, y, x ** y))