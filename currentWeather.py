import json

#James____________________________________________________________________________


def getJamesCWeath():
    with open("jamesWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        weather = current['weather']
        weath1 = weather[0]
        description = weath1['description']
        return description.title()

def getJamesCTemp():
    with open("jamesWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        temp_K = current['temp']
        temp_F = int((temp_K - 273) + 32)         #convert Kelvin to Fahrenheit
        return temp_F

def getJamesCWind():
    with open("jamesWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windSpeed_mps = current['wind_speed']
        windSpeed_mph = int(windSpeed_mps * 2.24)      #convert meters per second to miles per hour
        return windSpeed_mph

def getJamesCWindDir():
    with open("jamesWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windDir = current['wind_deg']
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
        
#Piankatank__________________________________________________________________________________

def getPiankCWeath():
    with open("piankWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        weather = current['weather']
        weath1 = weather[0]
        description = weath1['description']
        return description.title()

def getPiankCTemp():
    with open("piankWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        temp_K = current['temp']
        temp_F = int((temp_K - 273) + 32)             #convert Kelvin to Fahrenheit
        return temp_F

def getPiankCWind():
    with open("piankWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windSpeed_mps = current['wind_speed']
        windSpeed_mph = int(windSpeed_mps * 2.24)    #convert meters per second to miles per hour
        return windSpeed_mph

def getPiankCWindDir():
    with open("piankWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windDir = current['wind_deg']
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

#York __________________________________________________________________________________

def getYorkCWeath():
    with open("yorkWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        weather = current['weather']
        weath1 = weather[0]
        description = weath1['description']
        return description.title()

def getYorkCTemp():
    with open("yorkWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        temp_K = current['temp']
        temp_F = int((temp_K - 273) + 32)          #convert Kelvin to Fahrenheit
        return temp_F

def getYorkCWind():
    with open("yorkWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windSpeed_mps = current['wind_speed']
        windSpeed_mph = int(windSpeed_mps * 2.24)       #convert meters per second to miles per hour
        return windSpeed_mph

def getYorkCWindDir():
    with open("yorkWeatherWrites.py", 'r') as file:
        value = json.loads(file.read())
        current = value['current']
        windDir = current['wind_deg']
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
    print('James current weather:', getJamesCWeath())
    print('James current temperature:', getJamesCTemp(), 'F')
    print('James current wind speed:', getJamesCWind(), 'mph', getJamesCWindDir())
    print('Piankatank current weather:', getPiankCWeath())
    print('Piankatank current temperature:', getPiankCTemp(), 'F')
    print('Piankatank current wind speed:', getPiankCWind(), 'mph', getPiankCWindDir())
    print('York current weather:', getYorkCWeath())
    print('York current temperature:', getYorkCTemp(), 'F')
    print('York current wind speed:', getYorkCWind(), 'mph', getYorkCWindDir())
