# practice for loop
# Ask user name and count each character
# Uttam singh
name = input("Enter the name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]