import os
import csv
import json

API_KEY = os.environ['GOOGLE_API_KEY']
file_reader=csv.reader(open('sample.csv', 'rU'), dialect='excel')
f
or row in file_reader:
	street_address = row[4].replace(' ', '+')
	city, state, zip_code = row[5], row[6], row[7]
	print (street_address, city, state, zip_code)
	URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+{}&key={}'.format(street_address, city, state, API_KEY)
	print(URL)

# //Sample API call with address https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY