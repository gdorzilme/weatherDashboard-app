import requests
import configparser
from flask import Flask, render_template, request




# Open Weather App API function

def get_weather_results (cityname, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(cityname, api_key)
    r = requests.get(api_url) # request data from API URL
    return r.json() #return requested data as JSON
    print(api_url)

if __name__=='__main__':
    app.run()


print (get_weather_results("Vancouver", get_api_key()))
