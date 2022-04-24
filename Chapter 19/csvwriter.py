# Writer , DictWriter
from csv import writer

with open('file.csv1','w',newline='') as f:
    csv_writer = writer(f)

    # methods --> writerow and writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['Uttam','INDIA'])
    # csv_writer.writerow(['Shraddha','INDIA'])


    csv_writer.writerows([['Name','Country','Phone'],['Uttam','INDIA','9670064455'],['Shraddha','INDIA','8423854856']])