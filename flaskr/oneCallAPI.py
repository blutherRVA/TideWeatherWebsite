import requests
import keys2
import json

#Location Latitudes and Longitudes
james_lat = '37.5'
james_lon = '-77.4'
piank_lat ='37.5'
piank_lon = '-76.3'
york_lat = '37.3'
york_lon = '-76.4'



def james_weath(lat, long):
    # This is the URL that your login form points to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload

    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        session.post(post_login_url, data=payload)
        jsonf = session.get(request_url).json()
        with open("JamesWeatherWrites.py", 'w') as file:
            file.write(json.dumps(jsonf, indent=2))
        
def piank_weath(lat, long):
    # This is the URL that your login form points to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload

    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        session.post(post_login_url, data=payload)
        jsonf = session.get(request_url).json()
        with open("piankWeatherWrites.py", 'w') as file:
            file.write(json.dumps(jsonf, indent=2))

def york_weath(lat, long):
    # This is the URL that your login form points to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + long + '&appid=' + keys2.apiKey

    # Dictionary to create login payload

    payload = {
        'username': keys2.apiUserName,
        'pass': keys2.apiPassWord
    }

    with requests.Session() as session:
        session.post(post_login_url, data=payload)
        jsonf = session.get(request_url).json()
        with open("yorkWeatherWrites.py", 'w') as file:
            file.write(json.dumps(jsonf, indent=2))



if __name__ == "__main__":
    james_weath(james_lat, james_lon)
    piank_weath(piank_lat, piank_lon)
    york_weath(york_lat, york_lon)
    