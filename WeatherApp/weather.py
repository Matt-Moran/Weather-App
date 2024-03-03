#Weather App using Flask
 
import requests
from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime


key = '8cd65ea5db164a2a88d20600241402'

def get_current_weather(key, location):
   response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no').json()
   return response

def get_forecast(key, location, num_days=3):
   response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={num_days}&aqi=no&alerts=no').json()
   return response

#format a date from yyyy:mm:dd -> Month Day, Year
def format_date(date):
   date = datetime.strptime(date, "%Y-%m-%d")
   date = date.strftime("%B %d, %Y")
   return date

#input a date/time and return just the time
def format_time(time):
   time = datetime.strptime(time, "%Y-%m-%d %H:%M")
   time = time.strftime("%I:%M %p")
   return time

#input a date/time and return just the hour
def get_hour(time):
   time = datetime.strptime(time, "%Y-%m-%d %H:%M")
   time = time.strftime("%H")
   return time  


app = Flask(__name__) #Flask constructor

#Main Page
@app.route('/', methods=['POST', 'GET'])    
def mainPage():
   weather_data = None
   forecast = None
   if request.method == 'POST':
      location = request.form['location']
      weather_data = get_current_weather(key, location)
      forecast = get_forecast(key, location)
   return render_template('index.html', weather_data = weather_data, forecast = forecast, format_date = format_date, format_time = format_time)

#Raw data
#Normally something like this would not be included on an actual site, but I kept it just to help visualize the data that is sent by the API
@app.route('/alldata')
def allData():
   return get_forecast(key, 'Boston')

if __name__=='__main__':  
    app.run(debug = True)
