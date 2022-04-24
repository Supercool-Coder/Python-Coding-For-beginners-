name1 = ['Uttam','Dinesh','Anurag','Ankit']
name1.sort()
print(name1)

name2 = ('Uttam','Dinesh','Anurag','Ankit')
print(sorted(name2))

name3 = {'Uttam','Dinesh','Anurag','Ankit'}
print(sorted(name3))

guitars = [
    {'model' : 'yamaha f310','price':8400},
    {'model' : 'faith naptune','price':50000},
    {'model' : 'faith apollo venus','price':3500},
    {'model' : 'taylor 814','price':450000},
]
print(sorted(guitars , key = lambda d:d['price'],reverse = True))


# Reverse lagane se jo value guitars mein sab se jada hai wo pahele print hoga