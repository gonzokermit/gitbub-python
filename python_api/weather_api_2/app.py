from flask import Flask, render_template, request
import requests

api_key = ""

city_name = "berlin"
url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric".format(city_name,api_key)

data = requests.get(url).json()

description = data["list"][0]["weather"][0]["description"]
temp = data["list"][0]["main"]["temp"]

print(description)
print(temp)

