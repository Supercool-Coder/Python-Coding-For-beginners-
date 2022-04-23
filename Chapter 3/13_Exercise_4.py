# Problem
# Ask user to input a number containing more than one digit
# Example = 5555
# Calculate 5+5+5+5 and print

# algorithm - (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# example = 5555
# pick string charaacter one by one and change to int
# int (example[0]) + int(example[1]) ......go upto len(example)

addition = input("Enter the five numbers : ")
# addition = int(addition[i])+
total = 0
i = 0
while i < len(addition):
    total = total + int(addition[i])
    i = i + 1
print(total)