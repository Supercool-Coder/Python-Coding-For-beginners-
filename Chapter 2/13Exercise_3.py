# Take two comma separated inputs from user
# 1). User's name
# 2). A single character , "U"

# Output - 2 print lines
# 1). User's name length
# 2). Count the character that user inputed (bonus : case insensitive count)
name, char = input("Enter your name and character : ").split(",")
print(f"Lenght of your name is that : {len(name)}")
# print(f"Character count is that : {name.lower().count(char.lower())}")
print(f"Character count is that : {name.strip().lower().count(char.strip().lower())}")