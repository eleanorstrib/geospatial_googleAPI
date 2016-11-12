import os
import csv
import json
import requests
import time

MQ_API_KEY = os.environ.get('MQ_CONSUMER_KEY', '')
start_time = time.clock()
searched_locations = ''

file_reader=csv.reader(open('sample.csv', 'rU'), dialect='excel')
next(file_reader) # skip header row
row_no = 1

for row in file_reader:
    street_address, city, state, zip_code = row[4].replace(' ', '+'), row[5].replace(' ', '+'), row[6], row[7]
    searched_locations += "&location={},{},{},{}".format(street_address, city, state, zip_code)

URL = "https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1{}&key={}".format(searched_locations, MQ_API_KEY)
r_get = requests.get(URL)
info_dict = r_get.json()
data = info_dict['results']

for location in data:
    data_prefix = data[row_no-1]['locations'][0]
    latitude = data_prefix['latLng']['lat']
    longitude = data_prefix['latLng']['lng']
    location_type = data_prefix['geocodeQuality']
    print("Row #{}: latitude: {}, longitude: {}, location type: {}".format(
                                                                    row_no, latitude, longitude, location_type
                                                                    ))
    row_no +=1

print ("Program took {} seconds to execute".format((time.clock()-start_time)))
# sample https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1&location=Denver, CO&location=1555 Blake St, Denver, CO 80202&location=Boulder&key=KEY
