import time
import datetime

capeCharlesTimeStamp = 1592057307 #Low Tide morning of 6/13/2020 in Cape Charles Harbor


def tide_time_keeper(time_stamp):
    time_since_stamp = time.time() - time_stamp
    time_since_last_low = time_since_stamp % 44700

    if time_since_last_low <= 22350:
        nextHigh = int(22350 - time_since_last_low)
        slack_time = datetime.timedelta(seconds=nextHigh)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return "Next High Tide: " + str(time_print)



    elif time_since_last_low > 22350:
        nextLow = int(44700 - time_since_last_low)
        slack_time = datetime.timedelta(seconds=nextLow)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return "Next Low Tide: " + str(time_print)

    else:
        return "Calculation Error"




if __name__ == ('__main__'):
    print(time_keeper(capeCharlesTimeStamp))