from crypt import methods
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/kaset_sombun", methods=["GET"])
def index():

    api_key = ""

    city_name = "kaset sombun"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name,api_key)
    data = requests.get(url).json()

    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    

    return render_template("index.html", description=description,temp=temp,humidity=humidity,wind=wind)

if __name__ == "__main__":
    app.run()
