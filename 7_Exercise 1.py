# Make a function 'divide'
# divide (a,b)

def divide(x,y):
    try:
        return x/y

    # Hum ye massage khud se print krwa eahe hai aagr humko error wala massage hi print krwana hai toh uske liye
    # except ZeroDivisionError:
    except ZeroDivisionError as err:
        print(err)
        # print("Please don't divide by zero")
    except TypeError as err:
        print(err)
print(divide(4,2)) # 2


# This is a Zero division error
print(divide(4,0)) # Please don't divide by zero


# This is a Typeerror
print(divide('4',2)) # Please input numbers only