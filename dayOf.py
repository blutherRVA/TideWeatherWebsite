#Get today's date
import datetime
import time

dayToday = datetime.date.today()
timeC= datetime.datetime()

def DayOf(daysInFuture):
    dayObj = dayToday + datetime.timedelta(days=(daysInFuture))
    day = datetime.date.weekday(dayObj)

    if day == 0:
        return 'Monday'
    elif day == 1:
        return 'Tuesday'
    elif day == 2:
        return 'Wednesday'
    elif day == 3:
        return 'Thursday'
    elif day == 4:
        return 'Friday'
    elif day == 5:
        return 'Saturday'
    elif day == 6:
        return 'Sunday'
    else:
        return 'Error'

#def TimeOf(hoursFuture):
   # timeObj = timeC + datetime.timedelta(hours=hoursFuture)
    #return timeObj

if __name__ == ("__main__"):
    print(DayOf(1))
    print(timeC)
    
    


