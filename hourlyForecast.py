import json

riverj = "jamesWeatherWrites.py"
riverp = "piankWeatherWrites.py"
rivery = "yorkWeatherWrites.py"



def getHourWeather(river, time):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        hourly = value['hourly']
        hour = hourly[time]
        weather=hour['weather']
        weath1= weather[0]
        description = weath1['description']
        return description.title()

def getHourTemperature(river, time):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        hourly = value['hourly']
        hour = hourly[time]
        temp_K = hour['temp']
        temp_F = int((temp_K - 273) + 32)         #convert Kelvin to Fahrenheit
        return temp_F

def getHourWind(river, time):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        hourly = value['hourly']
        hour = hourly[time]
        windSpeed_mps = hour['wind_speed']
        windSpeed_mph = int(windSpeed_mps * 2.24)      #convert meters per second to miles per hour
        return windSpeed_mph

def getHourWindDir(river, time):
    with open(river, 'r') as file:
        value = json.loads(file.read())
        hourly = value['hourly']
        hour = hourly[time]
        windDir = hour['wind_deg']
        if 0 <= windDir < 45:
            return 'NNE'
        elif 45 <= windDir < 90:
            return 'ENE'
        elif 90 <= windDir < 135:
            return 'ESE'
        elif 135 <= windDir < 180:
            return 'SSE'
        elif 180 <= windDir < 225:
            return 'SSW'
        elif 225 <= windDir < 270:
            return 'WSW'    
        elif 270 <= windDir < 315:
            return 'WNW'
        elif 315 <= windDir < 360:
            return 'NNW'
        else:
            return 'No Wind Data'


if __name__ == "__main__":
    print(getHourWeather(riverj,2))
    print(getHourTemperature(riverj,2))
    print(getHourWind(riverj,2))
    print(getHourWindDir(riverj,2))