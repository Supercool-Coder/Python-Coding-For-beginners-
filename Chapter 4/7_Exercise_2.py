# Define is_palindrome function that take one word in starting as input and return true if it is palindrome else return
# false

# Palindrome ----> Word that reads same backwords as forwords

# Example
# is_palindrome("madam") -----> True
# is_palindrome("uttam") -----> False

# logic (algorinthm)
# step 1--> Reverse the string
# step 2--> Compare reversed string with original string

# def is_palindrome(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# print(is_palindrome("madam"))
# print(is_palindrome("uttam"))
# print(is_palindrome("naman"))


# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False
# print(is_palindrome("madam"))
# print(is_palindrome("uttam"))
# print(is_palindrome("naman"))

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("madam"))
print(is_palindrome("uttam"))
print(is_palindrome("naman"))