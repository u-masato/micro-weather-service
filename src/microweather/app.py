from flask import Flask, redirect, url_for

from microweather.settings import BASE_URL, CITY_ID, API_KEY
from microweather.weather import call_weather_api
from microweather.weather import get_weather_data
from microweather.weather import write_weather_data_to_csv

app = Flask(__name__)

@app.route('/')
def weather_service():
    url = BASE_URL + 'id=' + CITY_ID + '&APPID=' + API_KEY
    weather_data_json = call_weather_api(url)
    if weather_data_json:
        weather_data = get_weather_data(weather_data_json)
        file_path = write_weather_data_to_csv(weather_data)
        return ','.join(map(str, weather_data))

    else:
        # TODO: add fail safe action
        return "error: can't get weather data"
        pass


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
