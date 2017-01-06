from request import get 
from pprint import pprint
import json


url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'


stations = get(url).json()['items']
