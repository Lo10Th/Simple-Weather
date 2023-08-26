import requests
from dotenv import load_dotenv
import os
import json


def config():
    load_dotenv()

config()

def weather_data_rain_True(city, request_hours):
    if not request_hours == 0:
        request_hours -= 1
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={os.getenv('API_KEY')}&q={city}"
    response = requests.get(url)
    if not response.status_code == 200:
        raise Exception("API request unsuccessful.")
    response = response.json()
    if request_hours < len(response["list"]):
        weather_type = response["list"][request_hours]["weather"][0]["main"]
        if weather_type == "Rain":
            return True
    return False

    
print(weather_data_rain_True("Wuppertal", 4))