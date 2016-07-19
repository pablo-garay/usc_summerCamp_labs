print("""Team #1
-------""")

safety1 = int(input("Enter the number of safeties: "))
field_goal1 = int(input("Enter the number of field goals: "))
touchdown1 = int(input("Enter the number of touchdowns: "))

print("""Team #2
-------""")

safety2 = int(input("Enter the number of safeties: "))
field_goal2 = int(input("Enter the number of field goals: "))
touchdown2 = int(input("Enter the number of touchdowns: "))

print("Team #1 Score – %d" %(2 * safety1 + 3 * field_goal1 + 7 * touchdown1))
print("Team #2 Score – %d" %(2 * safety2 + 3 * field_goal2 + 7 * touchdown2))