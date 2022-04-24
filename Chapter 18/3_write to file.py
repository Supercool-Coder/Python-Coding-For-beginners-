# Aagr humko apne file k aandr kuch likhna hai toh uske liye hum ---> w , a , r+ ye theeno mode use kr skte hai.

# w mode ---> w mode k use tab kiya jata hai jab file empty hoti hai
# with open('file1.txt','w') as f:
#     f.write('Hello ! Uttam sir how are welcom to my hotel sir.')


# a mode ---> a mode tab use krte jab jab humko hamare file k data mein kuch add krna hota hai.
# with open('file1.txt','a') as f:
#     f.write('\nHello ! Uttam sir how are welcom to my hotel sir.')

# r+ mode ---> r+ mode k use kr k hum apne file ko read bhi kr skte hai aur write bhi kr skte hai.
with open('file1.txt','r+') as f:
    f.seek(len(f.read()))
    f.write('\nHello ! Uttam sir how are welcom to my hotel sir.')
