import csv

with open('C:\\Users\\st200\\Desktop\python_csv', 'w') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)