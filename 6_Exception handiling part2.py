# using else and finally keywords

while True:
    try:
        number = int(input('Enter the any number :- '))

    except ValueError:
        print('Please enter the number not integer')
    except:
        print('Unexpectedd error....!')

    else:
        print(f'User input = {number}')
        break
    finally:
        print('Finally block......!')
