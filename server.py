from flask import Flask, render_template, request, url_for
from weather import get_weather_data
from waitress import serve

app = Flask(__name__)

@app.route('/home', methods=["GET"])
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not bool(city.strip()):
        city = "chennai"
    weather_data = get_weather_data(city)
    if weather_data["cod"] != 200:
        return render_template("city_not_found.html")
    return render_template("weather.html",
                            title = weather_data["name"],
                            status = weather_data["weather"][0]["description"],
                            temp = weather_data["main"]["temp"],
                            feels_like = weather_data["main"]["feels_like"])

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
