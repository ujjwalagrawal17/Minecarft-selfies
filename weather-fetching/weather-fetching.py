from requests import get 
from pprint import pprint
import json
from haversine import haversine


stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 21.050000
my_lon = 81.670000


all_stations = get(url).json()['items']
closest_stn = find_closest()


weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']
pprint(my_weather)


def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station