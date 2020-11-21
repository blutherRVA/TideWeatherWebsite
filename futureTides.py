#crontab starts at midnight each day

import time
import datetime
from timeConvert import dayInSeconds

dayTimeTimeStamp = 1602907205
capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor
jamesTimeStamp = capeCharlesTimeStamp + 27480 #Jmes River Locks 458 minutes behind cape charles
piankatankTimeStamp = capeCharlesTimeStamp + 3660 # Cherry points tide is 61 minutes behind cape charles
yorkTimeStamp = capeCharlesTimeStamp - 240  #York River Spit is 4 minutes behind the cape charles


def HighTideKeeper(tts):
    timeSinceTTS = time.time()- tts - 40000 # This was just to get the code to run, subract -4000 in the morning
    timeSinceLastLow = timeSinceTTS % 44700
    dayTime = 0
    hTideDict = dict()
    hTideList = ['d1h1','d1h2', 'd2h1', 'd2h2', 'd3h1', 'd3h2', 'd4h1', 'd4h2', 
        'd5h1', 'd5h2', 'd6h1', 'd6h2', 'd7h1', 'd7h2']
    tAdder = 0
    tideCount = 1
    iteration = 0
    if timeSinceLastLow <= 22350:
        nextHigh = int(22350 - timeSinceLastLow)  #6hrs 12.5 min, minus time since last low = time til next high
        for tide in hTideList:
            iteration +=1
            if tideCount == 1:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                tAdder += 44700
                dayTime += timeSinceMidnight + 44700
                tideCount = 2

            elif tideCount == 2 and dayTime < 86400:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                dayTime = 0
                tideCount = 1
                tAdder+=44700
            
            elif tideCount == 2 and dayTime >= 86400:
                tideCount=1
                dayTime = 0
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
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                tAdder += 44700
                dayTime += timeSinceMidnight + 44700
                tideCount = 2

            elif tideCount == 2 and dayTime < 86400:
                slackTimeFromEpoch = tts + timeSinceTTS + nextHigh + tAdder
                timeDayHigh = time.ctime(slackTimeFromEpoch)
                time_output = time.strptime(timeDayHigh)
                time_print = time.strftime("%H : %M", time_output)
                timeSinceMidnight = dayInSeconds(time_print)
                hTideDict[tide] = time_print
                dayTime = 0
                tideCount = 1
                tAdder+=44700
            
            elif tideCount == 2 and dayTime >= 86400:
                tideCount=1
                dayTime = 0
                continue 
            
            else:
                print("error")

        return hTideDict



def LowTideKeeper(tts):
    timeSinceTTS = time.time() - tts 
    timeSinceLastLow = timeSinceTTS % 44700
    dayTime = 0
    lTideDict = dict()
    lTideList = ['d1l2', 'd2l1', 'd2l2', 'd3l1', 'd312', 'd4l1', 'd4l2', 
        'd5l1', 'd5l2', 'd6l1', 'd6l2', 'd7l1', 'd7l2']
    tAdder = 0
    tideCount = 2
    nextLow = int(44700 + timeSinceLastLow)  #12hrs 25 min, plus time since last low = time til next low
    for tide in lTideList:
        if tideCount == 1:
            slackTimeFromEpoch = tts + timeSinceTTS + nextLow + tAdder
            timeDayLow = time.ctime(slackTimeFromEpoch)
            time_output = time.strptime(timeDayLow)
            time_print = time.strftime("%H : %M", time_output)
            timeSinceMidnight = dayInSeconds(time_print)
            lTideDict[tide] = time_print
            tAdder += 44700
            dayTime += timeSinceMidnight + 44700
            tideCount = 2

        elif tideCount == 2 and dayTime < 86400:
            slackTimeFromEpoch = tts + timeSinceTTS + nextLow + tAdder
            timeDayLow = time.ctime(slackTimeFromEpoch)
            time_output = time.strptime(timeDayLow)
            time_print = time.strftime("%H : %M", time_output)
            timeSinceMidnight = dayInSeconds(time_print)
            lTideDict[tide] = time_print
            dayTime = 0
            tideCount = 1
            tAdder+=44700
        
        elif tideCount == 2 and dayTime >= 86400:
            tideCount=1
            dayTime = 0
            continue 
        
        else:
            print("error")

    return lTideDict

def combineLowAndHigh(tts):
    h = HighTideKeeper(tts)
    l = LowTideKeeper(tts)
    newTideDict = h.update(l)
    print(newTideDict)

if __name__=="__main__":
    #print(HighTideKeeper(piankatankTimeStamp))
    #print(LowTideKeeper(piankatankTimeStamp))
    combineLowAndHigh(piankatankTimeStamp)