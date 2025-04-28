# CHALLENGES WITH CSV FILES

# Challenge Consider the following Python list:

people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

# Using the CSV module write each element of the list (which is another list)
# into a CSV file called people1.csv
# After writing into the file, read and print out the file contents.
# Use the default , (comma) as the delimiter.

import csv

# writing a csv file
with open('plne/people1.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for peop in people:
        writer.writerow(peop)

# reading a csv file
with open('plne/people1.csv') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)

