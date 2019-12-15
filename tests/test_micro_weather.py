import sys

sys.path.append("../micro_weather")

import micro_weather

# from ../micro_weather/ import "micro-weather/micro_weather"

respons = micro_weather.call_weather_api()

def test_get_weather_data_01():
    pass

def test_get_weather_data_02():
    pass

def test_get_weather_data_csv_01():
    pass

def test_write_weather_data_to_csv_01():
    pass

#data = json_dict['dt'], json_dict['name'], json_dict['id'], \
#       json_dict['weather'][0]['main'], json_dict['weather'][0]['description'], \
#       json_dict['main']['temp'], json_dict['main']['humidity'], json_dict['wind']['speed']
