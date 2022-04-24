# Exception handling ---> wo error jo hamare pass execution k time aati hai

# using try and expect methods

while True:
    try:
        age = int(input('Enter the your age :- '))
        break
    except ValueError:
        print('Invalid Error , Maybe you entered string instesd of number , try again')

    except:
        print('Unexpectedd error.....')

if age < 20:
    print('You are teen ager you cannot play this game')

else:
    print('You can play this game ')
