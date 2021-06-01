import requests
import configparser
from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')   #Calls the function and render it at the homepage URL
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    cityname = request.form['cityName']  #variable coming from Flask
    api_key = get_api_key()

    data = get_weather_results(cityname, api_key)  #Pass in the city and API key
    temp = "{0:.2f}".format(data["main"]["temp"]) #formatted temperature to 2 decimal places
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])  #formatted feels like temp to 2 decimal places
    weather = data["weather"][0]["main"]
    location = data["name"]



def get_api_key():
    config = configparser.ConfigParser()
    config.read(f'config.ini')
    return config['openweathermap']['api']


# Open Weather App API function

def get_weather_results (cityname, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(cityname, api_key)
    r = requests.get(api_url) # request data from API URL
    return r.json() #return requested data as JSON
    print(api_url)

if __name__=='__main__':
    app.run()


print (get_weather_results("Vancouver", get_api_key()))
