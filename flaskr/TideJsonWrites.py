import time
import datetime
from timeConvert import dayInSeconds
from futureTides import HighTideKeeper, LowTideKeeper
import json

dayTimeTimeStamp = 1602907205
capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor
jamesTimeStamp = capeCharlesTimeStamp + 27480 #Jmes River Locks 458 minutes behind cape charles
piankatankTimeStamp = capeCharlesTimeStamp + 3660 # Cherry points tide is 61 minutes behind cape charles
yorkTimeStamp = capeCharlesTimeStamp - 240  #York River Spit is 4 minutes behind the cape charles

def mergeDict(hDict, lDict):
    return {**hDict, **lDict}


#jDict = {'a': '44', 'b' : '77', 'c': '23'}



if __name__ == ('__main__'):
    with open('jTide.json', 'w') as f1:
        json.dump(mergeDict(HighTideKeeper(jamesTimeStamp), LowTideKeeper(jamesTimeStamp)), f1, indent=2) 
    with open('pTide.json', 'w') as f2:
        json.dump(mergeDict(HighTideKeeper(piankatankTimeStamp), LowTideKeeper(piankatankTimeStamp)), f2, indent=2) 
    with open('yTide.json', 'w') as f3:
        json.dump(mergeDict(HighTideKeeper(yorkTimeStamp), LowTideKeeper(yorkTimeStamp)), f3, indent=2) 