from bs4 import BeautifulSoup
import requests
import subprocess
from datetime import date

def clear_screen():
	subprocess.run(["clear"])

def date_today():
	today = date.today()
	date_today = today.strftime("%d.%m.%Y")
	print(date_today)

def sunrise():
	url = "https://sonnenaufgang.online/sun/kaset_sombun"
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"html.parser")

	sunrise_data = soup.find("span",{"data-name":"sunrise"})
	sunrise_data = sunrise_data.text
	sunset_data = soup.find("span",{"data-name":"sunset"})
	sunset_data = sunset_data.text
	print("Sonnenaufgang         : {}".format(sunrise_data))
	print("Sonnenuntergang       : {}".format(sunset_data))

clear_screen()

city_name = input("Please enter a City-Name: ")
#city_name = "kaset sombun"

api_key = ""
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name,api_key)
data = requests.get(url).json()

country_code = data["sys"]["country"]

if country_code == "TH":
	country = "Thailand"
else:
	country = country_code

temperatur = data["main"]["temp"]

print("Wetterdaten für {} / {}".format(country.upper(),city_name.upper()))
date_today()
sunrise()
print("Aktuelle Temperatur   : {}".format(temperatur))


