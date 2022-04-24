# import pdb module
# module ---> Python files contains usefull classes and functions wrote by developer.

# According to wikipedia ---> Debugging is the process of finding and resolving defects or problem within a computer
# program that prevent correct operation of computer software or a system.

# Why debugging
# 1). Our program is not running and causing unexpected errors.
# 2). Our program is working fine but not working the same way we want.


# Step for debugging
# 1). Set trace
# 2). Execute code line by line

import pdb # This module is used for debugging.

pdb.set_trace()

name = input("Enter the your name :- ")
age = input("Enter the your age :- ")
print(f"Your name is {name} and age is {age}")
age2= int(age) + 5
print(f"{name} you will be  {age2} in next five years")


# l ---> List show krne k liye hamara jo code h wo kaha pr ruka hai
# q ---> iska mtlb num quit krna chahte hai
# c ---> apne code ko normally run krna chahte hai toh c command k use krte hai