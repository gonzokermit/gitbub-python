from crypt import methods
from time import strftime
from flask import Flask,render_template,request
import requests
import pytz
import datetime

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST","GET"])
def result():
    city_name = request.form["city_name"]

    time_zone = pytz.timezone("ASIA/BANGKOK")
    date_time = datetime.datetime.now(time_zone).strftime("%d.%m.%Y - %H.%M")

    api_key = ""
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name,api_key)
    data = requests.get(url).json()

    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    return render_template("result.html", date_time=date_time,city_name=city_name,description=description,temp=temp,humidity=humidity,wind=wind)

if __name__ == "__main__":
    app.run()
