#Starting from scratch using Git in VSCODE
from flask import Flask, render_template, request, url_for
import currentWeather
from dayOf import DayOf


app = Flask(__name__)

#Latitude and longitude inputs
lat_james = '37.5'
lon_james = '-77.4'
lat_piank = '37.5'
lon_piank = '-76.3'
lat_york = '37.3'
lon_york = '-76.4'

#days
day0 = DayOf(0)
day1 = DayOf(1)
day2 = DayOf(2) 
day3 = DayOf(3)
day4 = DayOf(4)
day5 = DayOf(5)
day6 = DayOf(6)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/james')
def james():
    weath = currentWeather.getJamesCWeath()
    temp = currentWeather.getJamesCTemp()
    wind = currentWeather.getJamesCWind()
    wdir = currentWeather.getJamesCWindDir()
    
    return render_template('james.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, day6=day6)

@app.route('/piankatank')
def piankatank():
    weath = currentWeather.getJamesCWeath()
    temp = currentWeather.getJamesCTemp()
    wind = currentWeather.getJamesCWind()
    wdir = currentWeather.getJamesCWindDir()
    return render_template('piankatank.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, day6=day6)

@app.route('/york')
def york():
    weath = currentWeather.getJamesCWeath()
    temp = currentWeather.getJamesCTemp()
    wind = currentWeather.getJamesCWind()
    wdir = currentWeather.getJamesCWindDir()
    return render_template('york.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, day6=day6)


if __name__ == "__main__":
    app.run(debug=True)
