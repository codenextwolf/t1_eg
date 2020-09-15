from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/weather/<city>")
def weather(city):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=fd17cc9947def5ecf47598af2c5b5821"
    response = requests.get(api_url)
    response_json = response.json()
    forecast = response_json.get("weather")[0].get("description")
    temperature = response_json.get("main").get("temp")
    return render_template("weather.html", 
                            city=city, 
                            forecast=forecast,
                            temperature=temperature)

@app.route("/covid/<country>")
def covid(country):
    api_url = "https://api.covid19api.com/summary"
    response = requests.get(api_url)
    response_json = response.json()
    global_stats = response_json.get("Global")
    globalCases = global_stats.get("TotalConfirmed")
    globalDeaths = global_stats.get("TotalDeaths")
    globalRecoveries = global_stats.get("TotalRecovered")

    countries = response_json.get("Countries")
    countryCases = 0
    countryDeaths = 0
    countryRecoveries = 0
    for country_obj in countries:
        c = country_obj.get("Country")
        if c == country:
            countryCases = country_obj.get("TotalConfirmed")
            countryDeaths = country_obj.get("TotalDeaths")
            countryRecoveries = country_obj.get("TotalRecovered")
    return render_template("covid.html", **locals())