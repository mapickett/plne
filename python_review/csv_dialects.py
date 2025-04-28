# WORKING WITH CSV DIALECTS

import csv
# with open('plne/passwd', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)

# dialects describe format of the csv file
# print(csv.list_dialects())

csv.register_dialect(
    'hashes', 
    delimiter='#', 
    quoting=csv.QUOTE_NONE,
    lineterminator='\n'
)

with open('plne/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for row in reader:
        print(row)

with open('plne/items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))