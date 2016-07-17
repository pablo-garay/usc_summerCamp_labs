print("******")
print("*    *")
print("*    *")
print("******")

print(" ____ ")
print("|    |")
print("|    |")
print("|    |")
print("|____|")

print("  ooo  ")
print(" o   o ")
print("o     o")
print(" o   o ")
print("  ooo  ")

print("  /\\")
print(" /  \\")
print("/____\\")

# Generate square shape in a single print statement
print("*" * 6 + "\n" +
      ("*" + " " * 4 + "*" + "\n") * 2 +
      "*" * 6 + "\n"
     )

# Generate rectangle shape in a single print statement
print(" " + "_" * 4 + " " + "\n" +
      ("|" + " " * 4 + "|" +  "\n") * 3 +
       "|" + "_" * 4 + "|"  +  "\n"
      )

# Generate circle shape in a single print statement
print("%s\n"
      "%s\n"
      "%s\n"
      "%s\n"
      "%s" %("  ooo  ", " o   o ", "o     o", " o   o ", "  ooo  "))

# Generate triangle shape in a single print statement
print("  /\\" + "\n" +
      " /  \\" + "\n" +
      "/____\\"
      )