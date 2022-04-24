from csv import DictReader

# Ordered dict
with open('file.csv','r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['name'])