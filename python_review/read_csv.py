# Using CSV stadnard library module

import csv

with open('plne/airtravel.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip the first line
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
# print(year_1958)

max_1958 = max(year_1958.values())
# print(max_1958)

for k, v in year_1958.items():
    if max_1958 == v:
        print(f'Busiest month in 1958:{k}, Flights:{v.strip()}')
