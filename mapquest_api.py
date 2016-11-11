import os
import csv
import json
import requests

searched_locations = ''

MQ_API_KEY = os.environ.get('MQ_CONSUMER_KEY', '')

file_reader=csv.reader(open('sample.csv', 'rU'), dialect='excel')
next(file_reader) # skip header row
row_no = 1

for row in file_reader:
    street_address, city, state, zip_code = row[4].replace(' ', '+'), row[5].replace(' ', '+'), row[6], row[7]
    searched_locations += "&location={},{},{},{}".format(street_address, city, state, zip_code)

URL = "https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1{}&key={}".format(searched_locations, MQ_API_KEY)
r_get = requests.get(URL)
info_dict = r_get.json()

print (info_dict)
# sample https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1&location=Denver, CO&location=1555 Blake St, Denver, CO 80202&location=Boulder&key=KEY
