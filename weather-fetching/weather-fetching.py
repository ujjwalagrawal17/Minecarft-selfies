from requests import get 
from pprint import pprint
import json
from haversine import haversine


stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/2024689'

my_lat = 52.194504
my_lon = 0.134708


all_stations = get(url).json()['items']

for station in all_stations:
    print(station)

pprint(stations)






def find_closest():
    smallest = 20036