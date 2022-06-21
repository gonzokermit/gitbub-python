import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://sonnenaufgang.online/sun/kaset_sombun"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

sunrise_data = soup.find("span",{"data-name":"sunrise"})
sunrise_data_nur_text = sunrise_data.text

sunset_data = soup.find("span",{"data-name":"sunset"})
sunset_data_nur_text = sunset_data.text

print("Kaset Sombun: Sonnenaufgang   = {}".format(sunrise_data_nur_text))
print("              Sonnenuntergang = {}".format(sunset_data_nur_text))
