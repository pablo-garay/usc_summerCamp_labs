print("\t\t\t\t\t\tPower")
print ("\t\t", end="")
title_array = list("Number")

# print number headers
for i in range(0, 6):
    print(" %4d\t\t" %i, end=""),

print("")
print("\t\t", end="")

for i in range(0, 6):
    print("   ---", end="\t\t")

# print rows
for i in range(0, 6):
    print("")
    print("%c\t%d\t" %(title_array[i], i), end="")

    for j in range(0, 6):
        print(" %4d" %(i ** j), end="\t\t")