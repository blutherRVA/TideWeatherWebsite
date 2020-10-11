import datetime

dt = 1602432000
dtf = datetime.date.fromtimestamp(dt)
print(dtf)

day = datetime.date.weekday(dtf)
print(day)