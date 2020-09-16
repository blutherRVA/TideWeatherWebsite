#Starting from scratch using Git in VSCODE
from flask import Flask, render_template, request, url_for
import weatherScraper


app = Flask(__name__)

#Latitude and longitude inputs
lat_james = '37.5'
lon_james = '-77.4'
lat_piank = '37.5'
lon_piank = '-76.3'
lat_york = '37.3'
lon_york = '-76.4'


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/james')
def james():
    weath = weather_scraper.weath(lat_james, lon_james)
    wind = int(float(weather_scraper.wind(lat_james, lon_james)) * 2.23) #converting m/s to mph
    wdir = weatherScraper.wind_dir(lat_james, lon_james)
    return render_template('james.html', weather=weath, wind=wind, windDir=wdir)

@app.route('/piankatank')
def piank():
    weath = weather_scraper.weath(lat_piank, lon_piank)
    wind = int(float(weather_scraper.wind(lat_piank, lon_piank)) * 2.23) #converting m/s to mph
    wdir = weatherScraper.wind_dir(lat_piank, lon_piank)
    return render_template('piankatank.html', weather=weath, wind=wind, windDir=wdir)

@app.route('/york')
def york():
    return render_template('york.html')



if __name__ == "__main__":
    app.run(debug=True)
