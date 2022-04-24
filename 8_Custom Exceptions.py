# Python custom exceptions
# Question ---> Why custom exceptions?
# Answer ---> To increase the redability of the code.

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError("Name is to short :- ")

username = input("Enter the your name :- ")
validate(username)
print(f"Hello {username}")