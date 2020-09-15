from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/weather')
def weather():
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=Cleveland&temp=Farenheit&appid=fd17cc9947def5ecf47598af2c5b5821"
    response = requests.get(api_url)
    print(json.dumps(response.json(), indent=2))
    return ""

@app.route('/covid')
def covid():
    api_url = "https://api.covid19api.com/summary"
    response = requests.get(api_url)
    print(json.dumps(response.json(), indent=2))
    return ""