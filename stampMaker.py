import time
import datetime


tidal_james_delta = 360
piankatank_delta = 21480
york_delta = 28800


def stamp_maker(time_since_last_low):
    stamp = time.time() - time_since_last_low #time in seconds
    return stamp




if __name__ == ('__main__'):
    print(stamp_maker(tidal_james_delta))
    print(stamp_maker(piankatank_delta))
    print(stamp_maker(york_delta))