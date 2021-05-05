import http.client
import ast
from datetime import datetime, timedelta, timezone


def get_actual_weather_data(lat, lon):
    list = []
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "f7cbc33b86msh15d74892fcf8b61p14f6c8jsn5ac8c369d4d2",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    for j in range(5, 0, -1):
        day_before = datetime.now() - timedelta(j)
        timestamp = int(day_before.replace(tzinfo=timezone.utc).timestamp())

        conn.request("GET", "/onecall/timemachine?lat=" + str(lat) + "&lon=" + str(lon) + "&dt=" + str(timestamp),
                     headers=headers)

        res = conn.getresponse()
        data = res.read()
        dict = data.decode("utf-8")
        dict = ast.literal_eval(dict)
        min_temp = 330
        max_temp = 0
        sum = 0
        humidity_sum = 0
        wind_speed_sum = 0
        for i in range(0, 24):
            sum += dict["hourly"][i]["temp"]
            humidity_sum += dict["hourly"][i]["humidity"]
            wind_speed_sum += dict["hourly"][i]["wind_speed"]
            if (dict["hourly"][i]["temp"] < min_temp):
                min_temp = dict["hourly"][i]["temp"]
            if (dict["hourly"][i]["temp"] > max_temp):
                max_temp = dict["hourly"][i]["temp"]

        avg = sum / 24
        min_temp = min_temp - 273.15
        max_temp = max_temp - 273.15
        avg = avg - 273.15
        avg_humidity = humidity_sum / 24
        avg_wind_speed = wind_speed_sum / 24
        list += [max_temp, min_temp, avg, avg_humidity, avg_wind_speed]
    return list
