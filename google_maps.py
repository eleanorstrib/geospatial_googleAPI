import os
import csv
import json
import requests

API_KEY = os.environ['GOOGLE_API_KEY']
# Sample API call with address https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
file_reader=csv.reader(open('sample.csv', 'rU'), dialect='excel')
next(file_reader) # skip header row
row_no = 1

for row in file_reader:
	street_address, city, state, zip_code = row[4].replace(' ', '+'), row[5].replace(' ', '+'), row[6], row[7]
	URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+{}&key={}'.format(street_address, city, state, API_KEY)
	r_get = requests.get(URL)
	info_dict = r_get.json()
	if info_dict['status'] == 'OK':
		data = info_dict['results'][0]['geometry']
		location_type = data['location_type']
		lat, lng = data['location']['lat'], data['location']['lng']
		print("Row #{} - latitude: {}, longitude: {} , location type: {}".format(row_no, lat, lng, location_type))
	else:
		print ("there was an error with row {}".format(row_no))

	row_no += 1

# Sample API call with address https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
