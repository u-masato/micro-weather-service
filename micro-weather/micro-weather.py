import requests
import json
import csv
import time
import datetime

import settings

API_KEY = settings.API_KEY
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
CITY_ID = '1850147' # TOKYO
HEADER = 'dt', 'city name', 'city id', 'city name', 'city id', \
         'weather', 'weather description', \
         'temperature', 'humidity', 'wind speed'


def call_weather_api():
    url = BASE_URL + 'id=' + CITY_ID + '&APPID=' + API_KEY

    response = requests.get(url)

    if response.status_code != 200:
        return ""

    return response.text


def get_weather_data_csv(json_data):
    json_dict = json.loads(json_data)

    data = json_dict['dt'], json_dict['name'], json_dict['id'], \
           json_dict['weather'][0]['main'], json_dict['weather'][0]['description'], \
           json_dict['main']['temp'], json_dict['main']['humidity'], json_dict['wind']['speed']

    return data


def write_weather_data_to_csv(data):

    if not os.path.exists('./data'):
        os.mkdir('./data')

    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    f = open('./data/' + current_time + '_tokyo_weather.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')

    writer.writerow(HEADER)
    writer.writerow(data)
    f.close()


if __name__ == "__main__":

    weather_data_json = call_weather_api()

    if weather_data_json:
        weather_data_csv = get_weather_data_csv(weather_data_json)
        write_weather_data_to_csv(weather_data_csv)
