# Advanced Min () and Max () function

# number = [1,2,3,4,5]
# print(min(number))

# names = ['Uttam','Dinesh','Ankit','Anurag']
# print(max(names , key = lambda item: len(item)))

student = {
    'Uttam' : {'Score' :87, 'age':19},
    'Dinesh' : {'Score' : 85 , 'age' :19},
    'Ankit' : {'Score' : 86 , 'age' :19},
    'Anurag' : {'Score' : 90 , 'age' :19}
}
print(max(student , key = lambda item : student[item]['Score']))

student2 = [
    {'name' : 'Uttam','Score' :87, 'age':20},
    {'name' : 'Ankit','Score' :85, 'age':19},
    {'name' : 'Anurag','Score' :80, 'age':21},
    {'name' : 'Dinesh','Score' :89, 'age':22}
]
print(max(student2 , key = lambda item :item.get('Score')))