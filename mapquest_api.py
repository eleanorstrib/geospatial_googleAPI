import os
import csv
import json
import requests

MQ_API_KEY = os.environ.get('MQ_CONSUMER_KEY', '')
MQ_API_URL = "https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1&location=''&location=''&location=''&key="


# sample https://www.mapquestapi.com/geocoding/v1/batch?&inFormat=kvp&outFormat=json&thumbMaps=false&maxResults=1&location=Denver, CO&location=1555 Blake St, Denver, CO 80202&location=Boulder&key=KEY
