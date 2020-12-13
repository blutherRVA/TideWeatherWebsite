ith requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        wind = r.json()["wind"]
        wind_current = wind["deg"]
        if 0 <= wind_current < 90:
            return 'NE'
        elif 90 <= wind_current < 180:
            return 'SE'
        elif 180 <= wind_current < 270:
            return 'SW'
        elif 270 <= wind_current < 360:
            return 'NW'
        else:
            return 'No Wind Data'