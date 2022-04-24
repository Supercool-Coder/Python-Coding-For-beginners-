import csv
from csv import DictWriter

with open('final.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])

    # writerow , writerows
    csv_writer.writerow({
        'firstname': 'Uttam',
        'lastname': 'Singh',
        'age':20
    })
    csv_writer.writerow({
        'firstname':'Shraddha',
        'lastname':'singh',
        'age':20
    })

    # Writer -----> [dict , dict , dict]
    csv_writer.writerows([
        {'firstname':'Uttam','lastname':'Singh','age':20},
        {'firstname':'shraddha','lastname':'Singh', 'age':20}
    ])