import sys
import os
import unittest
import json
import glob
import shutil
import pytest

from microweather.settings import BASE_URL, API_KEY, CITY_ID, HEADER
from microweather.weather import call_weather_api
from microweather.weather import get_weather_data
from microweather.weather import write_weather_data_to_csv


class TestMicroWeather(unittest.TestCase):

    def test_call_weather_api_normal_01(self):
        url = BASE_URL + 'id=' + CITY_ID + '&APPID=' + API_KEY
        data  = call_weather_api(url)

        self.assertTrue(type(data), type(""))

        json_data = json.loads(data)

        # test response content
        self.assertTrue('dt' in json_data)
        self.assertTrue('name' in json_data)
        self.assertTrue('id' in json_data)
        self.assertTrue('weather' in json_data)
        self.assertTrue('main' in json_data)
        self.assertTrue('wind' in json_data)

        self.assertTrue('main' in json_data['weather'][0])
        self.assertTrue('description' in json_data['weather'][0])
        self.assertTrue('temp' in json_data['main'])
        self.assertTrue('humidity' in json_data['main'])
        self.assertTrue('speed' in json_data['wind'])


    def test_call_weather_api_wrong_01(self):

        wrong_url = "https://www.not_exist.com/"
        self.assertEqual(call_weather_api(wrong_url), "")

        wrong_CITY_ID = '9999'
        url = BASE_URL + 'id=' + wrong_CITY_ID + '&APPID=' + API_KEY
        self.assertEqual(call_weather_api(url), "")

        wrong_api_key = "xxx"
        url = BASE_URL + 'id=' + CITY_ID + '&APPID=' + wrong_api_key
        self.assertEqual(call_weather_api(url), "")


    def test_get_weather_data_01(self):
        json_data = '{"coord":{"lon":139.69,"lat":35.69}, \
                    "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}], \
                    "base":"stations","main":{"temp":278.04,"feels_like":272.91,"temp_min":274.82,"temp_max":282.59, \
                    "pressure":1028,"humidity":61},"visibility":10000,"wind":{"speed":4.1,"deg":10},"clouds":{"all":31}, \
                    "dt":1576424667,"sys":{"type":1,"id":8074,"country":"JP","sunrise":1576446234,"sunset":1576481352}, \
                    "timezone":32400,"id":1850147,"name":"Tokyo","cod":200}'

        expected = [1576424667, "Tokyo", 1850147, "Clouds", "scattered clouds", 278.04, 61, 4.1]

        self.assertEqual(get_weather_data(json_data), expected)


    def test_write_weather_data_to_csv_01(self):

        if os.path.exists('./data'):
            shutil.rmtree('./data')

        write_data = (1576424667, "Tokyo", 1850147, "Clouds", "scattered clouds", 278.04, 61, 4.1)
        expected_header = ','.join(map(str,HEADER))
        expected_data = ','.join(map(str, write_data))

        write_weather_data_to_csv(write_data)

        self.assertTrue(os.path.exists('./data'))

        with open(glob.glob('./data/*.csv')[0]) as f:
            l = f.readlines()
            self.assertEqual(expected_header, l[0].strip())
            self.assertEqual(expected_data, l[1].strip())


if __name__ == '__main__':
    unittest.main()
