print("""
F) Fahrenheit
C) Celsius
""")

system_type = input("What temperature system are you using? ")

while system_type.upper() not in ('F', 'C'):
    print("%s is not one of the options." %system_type)
    system_type = input("What temperature system are you using? ")

if system_type.upper() == 'F':
    temp = float(input("Enter the temperature in Fahrenheit: "))
    print("The temperature in Celsius is %f" %( (temp - 32) * 5/9) )

elif system_type.upper() == 'C':
    temp = float(input("Enter the temperature in Celsius: "))
    print("The temperature in Fahrenheit is %f." %( temp * (9 / 5) + 32 ))


