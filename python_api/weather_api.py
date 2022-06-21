import subprocess
import requests
from datetime import datetime

def line():
	print("-"*100)

def clear_screen():
	subprocess.run(["clear"])

clear_screen()
line()

date_time = datetime.now().strftime("%d-%m-%Y - %H:%M")

api_key = "c53e332dc516ab13f41651cb872a1a4e"
city = input("Please enter a Town: ")
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)
data = requests.get(url).json()
print(data)
country_code  = data["sys"]["country"]

if country_code == "TH":
	country = "Thailand"
else:
	country = country_code

temperatur = data["main"]["temp"]

print(date_time)
print("Die aktuelle Temperatur in {} / {} ist {} Grad.".format(city.upper(),country,temperatur))
