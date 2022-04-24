# Dictionary Comprehension
# square = {1:4, 2:4, 3:9}

# This method is a square methods

square1 = {num:num**2 for num in range(1,11)}
print(square1)



square2 = {f'square of {num} is':num**2 for num in range(1,11)}
print(square2)



square = {f'square of {num} is':num**2 for num in range(1,11)}
for u,s in square.items():
    print(f"{u} : {s}")


# This method is cout the charecter

string = 'Uttam singh'
word_count = {char:string.count(char) for char in string}
print(word_count)