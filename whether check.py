import requests
from pprint import pprint

API_key ="xxxxxxxx" # Use API which you will get by signing in into the website whoes URL is given below

city = input("Enter City Name : ")

url = "https //api.openweathermap.org/data/2.5/weather?appid = " +API_key + "&q = "+ city

weather_data = requests.get(url).json()

pprint(weather_data)