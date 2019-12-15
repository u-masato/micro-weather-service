# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY_ID = '1850147' # TOKYO
HEADER = 'dt', 'city name', 'city id', 'city name', 'city id', \
         'weather', 'weather description', \
         'temperature', 'humidity', 'wind speed'
