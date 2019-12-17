from flask import Flask, redirect, url_for
import os
import settings
import micro_weather as weather

app = Flask(__name__)

@app.route('/')
def weather_service():
    url = settings.BASE_URL + 'id=' + settings.CITY_ID + '&APPID=' + settings.API_KEY
    weather_data_json = weather.call_weather_api(url)
    if weather_data_json:
        weather_data = weather.get_weather_data(weather_data_json)
        file_path = weather.write_weather_data_to_csv(weather_data)
        return ','.join(map(str, weather_data))

    else:
        # TODO: add fail safe action
        return "error: can't get weather data"
        pass


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
