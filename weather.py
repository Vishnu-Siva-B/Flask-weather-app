import requests
from dotenv import load_dotenv
import os 
from pprint import pprint

load_dotenv()

def get_weather_data(city):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&units=metric&q={city}'
    weather_data = requests.get(request_url).json()
    return weather_data
