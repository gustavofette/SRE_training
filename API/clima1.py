import requests
import json

api_key = "58690c20f5e453aa44e6e4239b983e0d"
weather_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Please choose your city:")

response = requests.get(weather_url, params={"q": city, "appid": api_key})
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"] - 273
    print("\nLa temperatura en",city, "es:", "{0:.2f}".format(temp), "Celcius\n")
else:
    print(data["message"]) 

