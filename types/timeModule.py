import time
import calendar

local = time.ctime(time.time())
print(time.time())
print(local)
print(time.localtime())

print(calendar.month(1998,2))
calendar.setfirstweekday(6)
print(calendar.month(1998,2))

print(calendar.isleap(2000))

print(calendar.calendar(2019))