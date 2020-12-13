#Main application file, connects templates with back end Python code using Flask
from flask import Flask, render_template, request, url_for 
import currentWeather 
from dayOf import DayOf, TimeOf 
from hourlyForecast import getHourWeather, getHourTemperature, getHourWind, getHourWindDir
from dailyForecast import getDailyWeather, getDailyTemperature, getDailyWind, getDailyWindDir
from tideTimeKeeper import tide_time_keeper
from TideJsonReads import jTideReads, pTideReads, yTideReads 


app = Flask(__name__)

#Tide Time Stamps
capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor
jamesTimeStamp = capeCharlesTimeStamp + 27480 #Jmes River Locks 458 minutes behind cape charles
piankatankTimeStamp = capeCharlesTimeStamp + 3660 # Cherry points tide is 61 minutes behind cape charles
yorkTimeStamp = capeCharlesTimeStamp - 240  #York River Spit is 4 minutes behind the cape charles

#Hourly forecast, every two hours for an 8 hour forecast
time2 = TimeOf(2)
time4 = TimeOf(4)
time6 = TimeOf(6)
time8 = TimeOf(8)

#7 day, daily average forecast
day0 = DayOf(0)
day1 = DayOf(1)
day2 = DayOf(2) 
day3 = DayOf(3)
day4 = DayOf(4)
day5 = DayOf(5)
day6 = DayOf(6)

#attached variables to each river's weather json 
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
    #7 day forecast, letter/number represent cell position
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
    #Next slack tide 
    nextTide = tide_time_keeper(jamesTimeStamp)
    #Future Tides
    d1h1 = jTideReads('d1', 'h1')
    d1h2 = jTideReads('d1', 'h2')
    d2h1 = jTideReads('d2', 'h1')
    d2h2 = jTideReads('d2', 'h2')
    d3h1 = jTideReads('d3', 'h1')
    d3h2 = jTideReads('d3', 'h2')
    d4h1 = jTideReads('d4', 'h1')
    d4h2 = jTideReads('d4', 'h2')
    d5h1 = jTideReads('d5', 'h1')
    d5h2 = jTideReads('d5', 'h2')
    d6h1 = jTideReads('d6', 'h1')
    d6h2 = jTideReads('d6', 'h2')
    d7h1 = jTideReads('d7', 'h1')
    d7h2 = jTideReads('d7', 'h2')
    d1l1 = jTideReads('d1', 'l1')
    d1l2 = jTideReads('d1', 'l2')
    d2l1 = jTideReads('d2', 'l1')
    d2l2 = jTideReads('d2', 'l2')
    d3l1 = jTideReads('d3', 'l1')
    d3l2 = jTideReads('d3', 'l2')
    d4l1 = jTideReads('d4', 'l1')
    d4l2 = jTideReads('d4', 'l2')
    d5l1 = jTideReads('d5', 'l1')
    d5l2 = jTideReads('d5', 'l2')
    d6l1 = jTideReads('d6', 'l1')
    d6l2 = jTideReads('d6', 'l2')
    d7l1 = jTideReads('d7', 'l1')
    d7l2 = jTideReads('d7', 'l2')

    
    return render_template(
        'james.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, 
        day6=day6, time2=time2, time4=time4, time6=time6, time8=time8, hrlyA1=hrlyA1, hrlyA2=hrlyA2, hrlyA3=hrlyA3, hrlyA4=hrlyA4, hrlyB1=hrlyB1,
        hrlyB2=hrlyB2, hrlyB3=hrlyB3, hrlyB4=hrlyB4, hrlyC1=hrlyC1, hrlyC2=hrlyC2, hrlyC3=hrlyC3, hrlyC4=hrlyC4, hrlyD1=hrlyD1, hrlyD2=hrlyD2, hrlyD3=hrlyD3,
        hrlyD4=hrlyD4, dailyA1=dailyA1, dailyA2=dailyA2, dailyB1=dailyB1, dailyB2=dailyB2, dailyC1=dailyC1, dailyC2=dailyC2, dailyD1=dailyD1,
        dailyD2=dailyD2, dailyE1=dailyE1, dailyE2=dailyE2, dailyF1=dailyF1, dailyF2=dailyF2, dailyG1= dailyG1, dailyG2=dailyG2, nextTide=nextTide,
        d1h1=d1h1, d1h2=d1h2, d2h1=d2h1, d2h2=d2h2, d3h1=d3h1, d3h2=d3h2, d4h1=d4h1, d4h2=d4h2, d5h1=d5h1, d5h2=d5h2, d6h1=d6h1, d6h2=d6h2, 
        d7h1=d7h1, d7h2=d7h2, d1l1=d1l1, d1l2=d1l2, d2l1=d2l1, d2l2=d2l2, d3l1=d3l1, d3l2=d3l2, d4l1=d4l1, d4l2=d4l2, d5l1=d5l1, d5l2=d5l2, d6l1=d6l1, d6l2=d6l2,
        d7l1=d7l1, d7l2=d7l2)

@app.route('/piankatank')
def piankatank():
     #current weather
    weath = currentWeather.getPiankCWeath()
    temp = currentWeather.getPiankCTemp()
    wind = currentWeather.getPiankCWind()
    wdir = currentWeather.getPiankCWindDir()
    #Hour by Hour forecast, letter/number represent cell position
    hrlyA1 = getHourWeather(riverp, 2)
    hrlyA2 = getHourTemperature(riverp, 2)
    hrlyA3 = getHourWind(riverp, 2)
    hrlyA4 = getHourWindDir(riverp, 2)
    hrlyB1= getHourWeather(riverp, 4)
    hrlyB2 = getHourTemperature(riverp, 4)
    hrlyB3 = getHourWind(riverp, 4)
    hrlyB4 = getHourWindDir(riverp, 4)
    hrlyC1= getHourWeather(riverp, 6)
    hrlyC2 = getHourTemperature(riverp, 6)
    hrlyC3 = getHourWind(riverp, 6)
    hrlyC4 = getHourWindDir(riverp, 6)
    hrlyD1= getHourWeather(riverp, 8)
    hrlyD2 = getHourTemperature(riverp, 8)
    hrlyD3 = getHourWind(riverp, 8)
    hrlyD4 = getHourWindDir(riverp, 8)
    #7 day forecast, letter/number represent cell position
    dailyA1 = getDailyWeather(riverp, 0)
    dailyA2 = getDailyWind(riverp, 0)
    dailyB1 = getDailyWeather(riverp, 1)
    dailyB2 = getDailyWind(riverp, 1)
    dailyC1 = getDailyWeather(riverp, 2)
    dailyC2 = getDailyWind(riverp, 2)
    dailyD1 = getDailyWeather(riverp, 3)
    dailyD2 = getDailyWind(riverp, 3)
    dailyE1 = getDailyWeather(riverp, 4)
    dailyE2 = getDailyWind(riverp, 4)
    dailyF1 = getDailyWeather(riverp, 5)
    dailyF2 = getDailyWind(riverp, 5)
    dailyG1 = getDailyWeather(riverp, 6)
    dailyG2 = getDailyWind(riverp, 6)
    #Next slack tide 
    nextTide = tide_time_keeper(piankatankTimeStamp)
    #Future Tides
    d1h1 = pTideReads('d1', 'h1')
    d1h2 = pTideReads('d1', 'h2')
    d2h1 = pTideReads('d2', 'h1')
    d2h2 = pTideReads('d2', 'h2')
    d3h1 = pTideReads('d3', 'h1')
    d3h2 = pTideReads('d3', 'h2')
    d4h1 = pTideReads('d4', 'h1')
    d4h2 = pTideReads('d4', 'h2')
    d5h1 = pTideReads('d5', 'h1')
    d5h2 = pTideReads('d5', 'h2')
    d6h1 = pTideReads('d6', 'h1')
    d6h2 = pTideReads('d6', 'h2')
    d7h1 = pTideReads('d7', 'h1')
    d7h2 = pTideReads('d7', 'h2')
    d1l1 = pTideReads('d1', 'l1')
    d1l2 = pTideReads('d1', 'l2')
    d2l1 = pTideReads('d2', 'l1')
    d2l2 = pTideReads('d2', 'l2')
    d3l1 = pTideReads('d3', 'l1')
    d3l2 = pTideReads('d3', 'l2')
    d4l1 = pTideReads('d4', 'l1')
    d4l2 = pTideReads('d4', 'l2')
    d5l1 = pTideReads('d5', 'l1')
    d5l2 = pTideReads('d5', 'l2')
    d6l1 = pTideReads('d6', 'l1')  
    d6l2 = pTideReads('d6', 'l2')
    d7l1 = pTideReads('d7', 'l1')
    d7l2 = pTideReads('d7', 'l2')

    return render_template('piankatank.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, 
        day6=day6, time2=time2, time4=time4, time6=time6, time8=time8, hrlyA1=hrlyA1, hrlyA2=hrlyA2, hrlyA3=hrlyA3, hrlyA4=hrlyA4, hrlyB1=hrlyB1,
        hrlyB2=hrlyB2, hrlyB3=hrlyB3, hrlyB4=hrlyB4, hrlyC1=hrlyC1, hrlyC2=hrlyC2, hrlyC3=hrlyC3, hrlyC4=hrlyC4, hrlyD1=hrlyD1, hrlyD2=hrlyD2, hrlyD3=hrlyD3,
        hrlyD4=hrlyD4, dailyA1=dailyA1, dailyA2=dailyA2, dailyB1=dailyB1, dailyB2=dailyB2, dailyC1=dailyC1, dailyC2=dailyC2, dailyD1=dailyD1,
        dailyD2=dailyD2, dailyE1=dailyE1, dailyE2=dailyE2, dailyF1=dailyF1, dailyF2=dailyF2, dailyG1= dailyG1, dailyG2=dailyG2, nextTide=nextTide,
        d1h1=d1h1, d1h2=d1h2, d2h1=d2h1, d2h2=d2h2, d3h1=d3h1, d3h2=d3h2, d4h1=d4h1, d4h2=d4h2, d5h1=d5h1, d5h2=d5h2, d6h1=d6h1, d6h2=d6h2, 
        d7h1=d7h1, d7h2=d7h2, d1l1=d1l1, d1l2=d1l2, d2l1=d2l1, d2l2=d2l2, d3l1=d3l1, d3l2=d3l2, d4l1=d4l1, d4l2=d4l2, d5l1=d5l1, d5l2=d5l2, d6l1=d6l1, d6l2=d6l2,
        d7l1=d7l1, d7l2=d7l2)


@app.route('/york')
def york():
     #current weather
    weath = currentWeather.getYorkCWeath()
    temp = currentWeather.getYorkCTemp()
    wind = currentWeather.getYorkCWind()
    wdir = currentWeather.getYorkCWindDir()
    #Hour by Hour forecast, letter/number represent cell position
    hrlyA1 = getHourWeather(rivery, 2)
    hrlyA2 = getHourTemperature(rivery, 2)
    hrlyA3 = getHourWind(rivery, 2)
    hrlyA4 = getHourWindDir(rivery, 2)
    hrlyB1= getHourWeather(rivery, 4)
    hrlyB2 = getHourTemperature(rivery, 4)
    hrlyB3 = getHourWind(rivery, 4)
    hrlyB4 = getHourWindDir(rivery, 4)
    hrlyC1= getHourWeather(rivery, 6)
    hrlyC2 = getHourTemperature(rivery, 6)
    hrlyC3 = getHourWind(rivery, 6)
    hrlyC4 = getHourWindDir(rivery, 6)
    hrlyD1= getHourWeather(rivery, 8)
    hrlyD2 = getHourTemperature(rivery, 8)
    hrlyD3 = getHourWind(rivery, 8)
    hrlyD4 = getHourWindDir(rivery, 8)
    #7 day forecast, letter/number represent cell position
    dailyA1 = getDailyWeather(rivery, 0)
    dailyA2 = getDailyWind(rivery, 0)
    dailyB1 = getDailyWeather(rivery, 1)
    dailyB2 = getDailyWind(rivery, 1)
    dailyC1 = getDailyWeather(rivery, 2)
    dailyC2 = getDailyWind(rivery, 2)
    dailyD1 = getDailyWeather(rivery, 3)
    dailyD2 = getDailyWind(rivery, 3)
    dailyE1 = getDailyWeather(rivery, 4)
    dailyE2 = getDailyWind(rivery, 4)
    dailyF1 = getDailyWeather(rivery, 5)
    dailyF2 = getDailyWind(rivery, 5)
    dailyG1 = getDailyWeather(rivery, 6)
    dailyG2 = getDailyWind(rivery, 6)
    #Next slack tide 
    nextTide = tide_time_keeper(yorkTimeStamp)
    #Future Tides
    d1h1 = yTideReads('d1', 'h1')
    d1h2 = yTideReads('d1', 'h2')
    d2h1 = yTideReads('d2', 'h1')
    d2h2 = yTideReads('d2', 'h2')
    d3h1 = yTideReads('d3', 'h1')
    d3h2 = yTideReads('d3', 'h2')
    d4h1 = yTideReads('d4', 'h1')
    d4h2 = yTideReads('d4', 'h2')
    d5h1 = yTideReads('d5', 'h1')
    d5h2 = yTideReads('d5', 'h2')
    d6h1 = yTideReads('d6', 'h1')
    d6h2 = yTideReads('d6', 'h2')
    d7h1 = yTideReads('d7', 'h1')
    d7h2 = yTideReads('d7', 'h2')
    d1l1 = yTideReads('d1', 'l1')
    d1l2 = yTideReads('d1', 'l2')
    d2l1 = yTideReads('d2', 'l1')
    d2l2 = yTideReads('d2', 'l2')
    d3l1 = yTideReads('d3', 'l1')
    d3l2 = yTideReads('d3', 'l2')
    d4l1 = yTideReads('d4', 'l1')
    d4l2 = yTideReads('d4', 'l2')
    d5l1 = yTideReads('d5', 'l1')
    d5l2 = yTideReads('d5', 'l2')
    d6l1 = yTideReads('d6', 'l1')  
    d6l2 = yTideReads('d6', 'l2')
    d7l1 = yTideReads('d7', 'l1')
    d7l2 = yTideReads('d7', 'l2')

    return render_template('york.html', weather=weath, temperature=temp, windSp=wind, windDir=wdir, day0=day0, day1=day1, day2=day2, day3=day3, day4=day4, day5=day5, 
        day6=day6, time2=time2, time4=time4, time6=time6, time8=time8, hrlyA1=hrlyA1, hrlyA2=hrlyA2, hrlyA3=hrlyA3, hrlyA4=hrlyA4, hrlyB1=hrlyB1,
        hrlyB2=hrlyB2, hrlyB3=hrlyB3, hrlyB4=hrlyB4, hrlyC1=hrlyC1, hrlyC2=hrlyC2, hrlyC3=hrlyC3, hrlyC4=hrlyC4, hrlyD1=hrlyD1, hrlyD2=hrlyD2, hrlyD3=hrlyD3,
        hrlyD4=hrlyD4, dailyA1=dailyA1, dailyA2=dailyA2, dailyB1=dailyB1, dailyB2=dailyB2, dailyC1=dailyC1, dailyC2=dailyC2, dailyD1=dailyD1,
        dailyD2=dailyD2, dailyE1=dailyE1, dailyE2=dailyE2, dailyF1=dailyF1, dailyF2=dailyF2, dailyG1= dailyG1, dailyG2=dailyG2, nextTide=nextTide,
        d1h1=d1h1, d1h2=d1h2, d2h1=d2h1, d2h2=d2h2, d3h1=d3h1, d3h2=d3h2, d4h1=d4h1, d4h2=d4h2, d5h1=d5h1, d5h2=d5h2, d6h1=d6h1, d6h2=d6h2, 
        d7h1=d7h1, d7h2=d7h2, d1l1=d1l1, d1l2=d1l2, d2l1=d2l1, d2l2=d2l2, d3l1=d3l1, d3l2=d3l2, d4l1=d4l1, d4l2=d4l2, d5l1=d5l1, d5l2=d5l2, d6l1=d6l1, d6l2=d6l2,
        d7l1=d7l1, d7l2=d7l2)


   
