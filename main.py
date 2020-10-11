
from tide_time_keeper import tide_time_keeper
import weather_updates
import weather_scraper



#Time Stamps
james = 1592399416 #Closest low tide from when program was written for James River Locks
piank = 1592378296 #Closest low tide from when program was written for Cherry Point on the Piankatank
mobjack = 1592370976 #Closest low tide from when program was written for the Severn River in Mobjack Bay

#Location Latitudes and Longitudes
james_lat = '37.5'
james_lon = '-77.4'
piank_lat ='37.5'
piank_lon = '-76.3'
mob_lat = '37.3'
mob_lon = '-76.4'



weather_updates.slack_update(tide_time_keeper(james), tide_time_keeper(piank), tide_time_keeper(mobjack))
weather_updates.weather_update(weather_scraper.weath(james_lat, james_lon), weather_scraper.weath(piank_lat, piank_lon), weather_scraper.weath(mob_lat, mob_lon))
weather_updates.wind_update(weather_scraper.wind(james_lat, james_lon), weather_scraper.wind_dir(james_lat, james_lon), weather_scraper.wind(piank_lat, piank_lon), weather_scraper.wind_dir(piank_lat, piank_lon), weather_scraper.wind(mob_lat, mob_lon), weather_scraper.wind_dir(mob_lat, mob_lon))



