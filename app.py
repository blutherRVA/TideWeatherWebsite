#Starting from scratch using Git in VSCODE
from flask import Flask, render_template, request, url_for
import currentWeather
from dayOf import DayOf, TimeOf
from hourlyForecast import getHourWeather, getHourTemperature, getHourWind, getHourWindDir
from dailyForecast import getDailyWeather, getDailyTemperature, getDailyWind, getDailyWindDir


app = Flask(__name__)


#Hourly forecast
time2 = TimeOf(2)
time4 = TimeOf(4)
time6 = TimeOf(6)
time8 = TimeOf(8)

#Daily forecast
day0 = DayOf(0)
day1 = DayOf(1)
day2 = DayOf(2) 
day3 = DayOf(3)
day4 = DayOf(4)
day5 = DayOf(5)
day6 = DayOf(6)

#River file

riverj = "jamesWeatherWrites.py"
riverp = "piankWeatherWrites.py"
rivery = "yorkWeatherWrites.py"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/james')
def james():
    #current weather
    weath = currentWeather.getJamesCWeath()
    temp = currentWeather.getJamesCTemp()
    wind = currentWeather.getJamesCWind()
    wdir = currentWeather.getJamesCWindDir()
    #Hour by Hour forecast, letter/number represent cell position
    hrlyA1 = getHourWeather(riverj, 2)
    hrlyA2 = getHourTemperature(riverj, 2)
    hrlyA3 = getHourWind(riverj, 2)
    hrlyA4 = getHourWindDir(riverj, 2)
    hrlyB1= getHourWeather(riverj, 4)
    hrlyB2 = getHourTemperature(riverj, 4)
    hrlyB3 = getHourWind(riverj, 4)
    hrlyB4 = getHourWindDir(riverj, 4)
    hrlyC1= getHourWeather(riverj, 6)
    hrlyC2 = getHourTemperature(riverj, 6)
    hrlyC3 = getHourWind(riverj, 6)
    hrlyC4 = getHourWindDir(riverj, 6)
    hrlyD1= getHourWeather(riverj, 8)
    hrlyD2 = getHourTemperature(riverj, 8)
    hrlyD3 = getHourWind(riverj, 8)
    hrlyD4 = getHourWindDir(riverj, 8)
    #Daily forecast for the week, letter/number represent cell position
    dailyA1 = getDailyWeather(riverj, 0)
    dailyA2 = getDailyWind(riverj, 0)
    dailyB1 = getDailyWeather(riverj, 1)
    dailyB2 = getDailyWind(riverj, 1)
    dailyC1 = getDailyWeather(riverj, 2)
    dailyC2 = getDailyWind(riverj, 2)
    dailyD1 = getDailyWeather(riverj, 3)
    dailyD2 = getDailyWind(riverj, 3)
    dailyE1 = getDailyWeather(riverj, 4)
    dailyE2 = getDailyWind(riverj, 4)
    dailyF1 = getDailyWeather(riverj, 5)
    dailyF2 = getDailyWind(riverj, 5)
    dailyG1 = getDailyWeather(riverj, 6)
    dailyG2 = getDailyWind(riverj, 6)
    
    return render_template(
        'james.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, 
        day6=day6, time2=time2, time4=time4, time6=time6, time8=time8, hrlyA1=hrlyA1, hrlyA2=hrlyA2, hrlyA3=hrlyA3, hrlyA4=hrlyA4, hrlyB1=hrlyB1,
        hrlyB2=hrlyB2, hrlyB3=hrlyB3, hrlyB4=hrlyB4, hrlyC1=hrlyC1, hrlyC2=hrlyC2, hrlyC3=hrlyC3, hrlyC4=hrlyC4, hrlyD1=hrlyD1, hrlyD2=hrlyD2, hrlyD3=hrlyD3,
        hrlyD4=hrlyD4, dailyA1=dailyA1, dailyA2=dailyA2, dailyB1=dailyB1, dailyB2=dailyB2, dailyC1=dailyC1, dailyC2=dailyC2, dailyD1=dailyD1,
        dailyD2=dailyD2, dailyE1=dailyE1, dailyE2=dailyE2, dailyF1=dailyF1, dailyF2=dailyF2, dailyG1= dailyG1, dailyG2=dailyG2
        )

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
