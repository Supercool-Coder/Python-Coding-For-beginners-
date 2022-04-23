# Ask a user for name
# Example - Uttam
# print count of each words
name = input("Enter the name : ")
temp_var = ""
i = 0
while i<len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1