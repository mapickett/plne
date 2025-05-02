# CODING CHALLENGE - requests

# 1 Using requests connect to https://jsonplaceholder.typicode.com/users 
# and take the JSON encoded string in Python object
# 2 The resulting Python object will be a list of dictionaries. 
# Process the list and extract the following information for each user:
# Name, City, GPS coordinates in form of (LAT, LNG), Company name
# 3 Write to a CSV File a row for each user. The fields of the CSV file will be:
# name, city, GPS coordinates and company name
# For example for the first user you'll write in the CSV file: 
# Leanne Graham,Gwenborough,"(-37.3159,-37.3159)",Romaguera-Crona

import csv
import json
import requests

# getting the json data from the server
response = requests.get('https://jsonplaceholder.typicode.com/users')

# loading the json encoded string - list of dicts
users = json.loads(response.text)

# opening the csv file for writing
with open('python_review/users.csv', 'wt') as f:
    writer = csv.writer(f)

    # writing a header to the file
    writer.writerow(("Name", "City", "GPS", "Company"))

    # iterating over the user lisddt
    for user in users:
        # getting data and formatting
        name = user['name']
        city = user['address']['city']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        geo = f'({lat},{lng})'
        company_name = user['company']['name']

        # writing to csv file
        csvdata = (name, city, geo, company_name)
        writer.writerow(csvdata)
