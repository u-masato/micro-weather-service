import os
import time
import datetime
import requests
import json
import csv

from settings import BASE_URL
from settings import CITY_ID
from settings import API_KEY
from settings import HEADER


def call_weather_api(url):

    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return ""

    if response.status_code != 200:
        return ""

    return response.text


def get_weather_data(json_data):
    json_dict = json.loads(json_data)

    data = [
            json_dict['dt'], json_dict['name'], json_dict['id'], \
            json_dict['weather'][0]['main'], json_dict['weather'][0]['description'], \
            json_dict['main']['temp'], json_dict['main']['humidity'], json_dict['wind']['speed']
            ]

    return data


def write_weather_data_to_csv(data):

    if not os.path.exists('./data'):
        os.mkdir('./data')

    current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    csv_file = './data/' + current_time + '_tokyo_weather.csv'
    f = open(csv_file, 'w')

    try:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(HEADER)
        writer.writerow(data)
        f.close()
    except Exception as e:
        print(e)
        return ""

    return csv_file


if __name__ == "__main__":
    url = BASE_URL + 'id=' + CITY_ID + '&APPID=' + API_KEY
    weather_data_json = call_weather_api(url)
    if weather_data_json:
        weather_data_csv = get_weather_data(weather_data_json)
        write_weather_data_to_csv(weather_data_csv)
    else:
        # TODO: add fail safe action
        pass
