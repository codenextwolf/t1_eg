# t1_eg


### api_req_eg
Simple API request example/starter. 2 routes (/weather and /covid) that print weather and Covid data (OpenWeatherMap & Covid19Api) to the console. 

Dependencies:
- pip install flask
- pip install requests

### web_server_eg
Simple web server example/starter. Serves up static html/css files. There is also a route with dynamic content using Jinja templating at /(name) that will greet the (name).

Dependencies:
- pip install flask

### api_server_eg
Simple example/starter that brings the two above together. The route /weather/(city) will display the weather data for the (city) and /covid/(country) will display the covid data for the (country) from the APIs. 

Dependencies:
- pip install flask
- pip install requests
