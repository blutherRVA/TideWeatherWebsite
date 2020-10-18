import time
import datetime
from timeConvert import dayInSeconds


capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor

def funct(tts):
    timeSinceTTS = time.time()- tts - 40000
    timeSinceLastLow = timeSinceTTS % 44700
    dayTime = 0
    hTideDict = dict()
    hTideList = ['d1h2', 'd2h1', 'd2h2', 'd3h1', 'd3h2', 'd4h1', 'd4h2', 
        'd5h1', 'd5h2', 'd6h1', 'd6h2', 'd7h1', 'd7h2']
    tAdder = 0
    tideCount = 2
    iteration = 0
    if timeSinceLastLow <= 22350:
        nextHigh = int(22350 - timeSinceLastLow)  #6hrs 12.5 min, minus time since last low = time til next high
        for tide in hTideList:
            iteration +=1
            if tideCount == 1:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                print(tAdder)
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                tAdder += 44700
                dayTime += timeSinceMidnight + 44700
                tideCount = 2
                print("Tide 1")

            elif tideCount == 2 and dayTime < 86400:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                print(slackTimeFromEpoch)
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                dayTime = 0
                tideCount = 1
                tAdder+=44700
                print ("Tide 2")
            
            elif tideCount == 2 and dayTime >= 86400:
                tideCount=1
                dayTime = 0
                print("it continued @" + str(iteration))
                continue 
            
            else:
                print("error")
        return hTideDict


    elif timeSinceLastLow > 22350:
        nextHigh = int(67050 - timeSinceLastLow)  #18hrs 37.5 min, minus time since last low = time til next high
        for tide in hTideList:
            iteration +=1
            if tideCount == 1:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                print(tAdder)
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                tAdder += 44700
                dayTime += timeSinceMidnight + 44700
                tideCount = 2
                print("Tide 1")

            elif tideCount == 2 and dayTime < 86400:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                print(slackTimeFromEpoch)
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                dayTime = 0
                tideCount = 1
                tAdder+=44700
                print ("Tide 2")
            
            elif tideCount == 2 and dayTime >= 86400:
                tideCount=1
                dayTime = 0
                print("it continued @" + str(iteration))
                continue 
            
            else:
                print("error")
        return hTideDict

if __name__ == "__main__":
    print(funct(capeCharlesTimeStamp))