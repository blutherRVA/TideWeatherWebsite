import time
import datetime

capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor


timeSinceTTS = time.time()- capeCharlesTimeStamp
timeSinceLastLow = timeSinceTTS % 44700
nextHigh = int(22350 - timeSinceLastLow)  #6hrs 12.5 min, minus time since last low = time til next high
slackTimeFromEpoch = capeCharlesTimeStamp + timeSinceLastLow + nextHigh
slack_time = datetime.timedelta(seconds=nextHigh)
timeDayHigh = time.ctime(slackTimeFromEpoch)
time_output = time.strptime(timeDayHigh)
time_print = time.strftime("%H : %M", time_output)


def dayInSeconds(dayTime):
    HrMn= dayTime.split(':')
    for t in HrMn:
        seconds = (int(HrMn[0])*60*60) + ((int(HrMn[1]))*60)
    return seconds 

if __name__ == "__main__":
    print(dayInSeconds(time_print))
