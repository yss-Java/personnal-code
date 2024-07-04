import time
t=time.localtime()
print('t-->',t)
print('tm_year',t.tm_year)
print('tm_year-->',t[0])

print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.asctime(time.localtime()))
print(time.tzname)
# strftime 使用
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

import datetime
import time

print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.min)
print(datetime.date.max)

td = datetime.date.today()
print(td.replace(year=1945, month=8, day=15))
print(td.timetuple())
print(td.weekday())
print(td.isoweekday())
print(td.isocalendar())
print(td.isoformat())
print(td.strftime('%Y %m %d %H:%M:%S %f'))
print(td.year)
print(td.month)
print(td.day)

t = datetime.time(10, 10, 10)
print(t.isoformat())
print(t.replace(hour=9, minute=9))
print(t.strftime('%I:%M:%S %p'))
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.tzinfo)

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))
print(datetime.datetime.combine(datetime.date(2019, 12, 1), datetime.time(10, 10, 10)))
print(datetime.datetime.min)
print(datetime.datetime.max)


import datetime

td = datetime.datetime.today()
print(td.date())
print(td.time())
print(td.replace(day=11, second=10))
print(td.weekday())
print(td.isoweekday())
print(td.isocalendar())
print(td.isoformat())
print(td.strftime('%Y-%m-%d %H:%M:%S .%f'))
print(td.year)
print(td.month)
print(td.month)
print(td.hour)
print(td.minute)
print(td.second)
print(td.microsecond)
print(td.tzinfo)


import calendar

calendar.setfirstweekday(1)
print(calendar.firstweekday())
print(calendar.isleap(2023))
print(calendar.leapdays(1945, 2023))
print(calendar.weekday(2023, 12, 1))
print(calendar.monthrange(2023, 12))
print(calendar.month(2023, 12))
print(calendar.prcal(2019))


from calendar import Calendar

c = Calendar()
print(list(c.iterweekdays()))
for i in c.itermonthdates(2023, 12):
    print(i)

from calendar import TextCalendar

tc = TextCalendar()
print(tc.formatmonth(2023, 12))
print(tc.formatyear(2023))


from calendar import HTMLCalendar

hc = HTMLCalendar()
print(hc.formatmonth(2023, 12))
print(hc.formatyear(2023))
print(hc.formatyearpage(2023))