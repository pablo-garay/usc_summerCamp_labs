last_num = int(input("How large do you want your multiplication table to be? ")) + 1

#print number headers
print("\t\t", end="")
for i in range(1, last_num):
    print(" %d\t\t" %i, end=""),

print("")
print("\t\t", end="")

for i in range(1, last_num):
    print("---", end="\t\t")

for i in range(1, last_num):
    print("")
    print("%d\t|\t" % i, end="")

    for j in range(1, last_num):
        print(" %d" %(i * j), end="\t\t")
