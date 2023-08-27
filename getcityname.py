import requests
import os
from dotenv import load_dotenv

def config():
    load_dotenv()

def get_city_name(long, lat):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={long},{lat}&sensor=true&key={os.getenv('google_api_key')}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("API request unsuccessful.")
    
    data = response.json()
    return data['results'][0]['address_components'][3]["long_name"]

config()
