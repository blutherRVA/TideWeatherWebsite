import json

riverj = "jamesWeatherWrites.py"
riverp = "piankWeatherWrites.py"
rivery = "yorkWeatherWrites.py"



def getDailyWeather(river, dayInp):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        daily = value['daily']
        day = daily[dayInp]
        weather=day['weather']
        weath1= weather[0]
        description = weath1['description']
        return description.title()

def getDailyTemperature(river, dayInp):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        daily = value['daily']
        day = daily[dayInp]
        dayTemp = day['temp']
        temp_K = dayTemp['day']
        temp_F = int((temp_K - 273) + 32)         #convert Kelvin to Fahrenheit
        return temp_F

def getDailyWind(river, dayInp):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        daily = value['daily']
        day = daily[dayInp]
        windSpeed_mps = day['wind_speed']
        windSpeed_mph = int(windSpeed_mps * 2.24)      #convert meters per second to miles per hour
        return windSpeed_mph

def getDailyWindDir(river, dayInp):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        daily = value['daily']
        day = daily[dayInp]
        windDir = day['wind_deg']
        if 0 <= windDir < 90:
            return 'NE'
        elif 90 <= windDir < 180:
            return 'SE'
        elif 180 <= windDir < 270:
            return 'SW'
        elif 270 <= windDir < 360:
            return 'NW'
        else:
            return 'No Wind Data'


if __name__ == "__main__":
    print(getDailyWeather(riverj,0))
    print(getDailyTemperature(riverj,0))
    print(getDailyWind(riverj,0))
    print(getDailyWindDir(riverj,0))