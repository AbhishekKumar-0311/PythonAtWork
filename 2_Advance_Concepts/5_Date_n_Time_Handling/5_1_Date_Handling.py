# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:33:25 2020

@author: abhi0
"""

#from datetime import date
import datetime as dt


# date object of today's date
# Get current date
today = dt.date.today() 
print("Today:", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
# All the below date attributes are INT
ty=today.year
tm=today.month
td=today.day
print(type(td))


# Creation of Date object to represent a date
d = dt.date(2019, 4, 13)
print(d)
d = dt.date(ty, tm, td)
print(d)

# Get date from a timestamp
# Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC
timestamp = dt.date.fromtimestamp(1326244364)
print("Date =", timestamp)


# Present date and time
dtm = dt.datetime.now()
print(dtm)
print("Current year:", dtm.year)
print("Current month:", dtm.month)
print("Current day:", dtm.day)
# All the below date attributes are INT
ty=dtm.year
tm=dtm.month
td=dtm.day
print("hour =", dtm.hour)
print("minute =", dtm.minute)
print("timestamp =", dtm.timestamp())



# Print year, month, hour, minute and timestamp
dtm=dt.datetime(2019, 4, 13)
print(dtm)

dtm=dt.datetime(2017, 11, 28, 23, 55, 59, 342380)
print(dtm)
ty=dtm.year
tm=dtm.month
td=dtm.day
th=dtm.hour
tm=dtm.minute
ts=dtm.second
tt=dtm.timestamp()
print("hour =", dtm.hour)
print("minute =", dtm.minute)
print("timestamp =", dtm.timestamp())
print(ts)


# To get time
tm=dt.time()
print(tm)
# time(hour, minute, second
tm = dt.time(11, 34, 56)
print(tm)
# time(hour, minute, second, microsecond)
tm = dt.time(11, 34, 56, 234566)
print("d =", tm)

print("hour =", tm.hour)
print("minute =", tm.minute)
print("second =", tm.second)
print("microsecond =", tm.microsecond)


# Timedelta
#from datetime import timedelta

t1 = dt.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = dt.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print(t3.day)


#Python strftime() - datetime object to string
# The method creates a formatted string from a given date, datetime or time object.
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# Python strptime() - string to datetime
# It creates a datetime object from a given string (representing date and time).

from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# datetime to string using strftime() AGAIN
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)


# Python datetime to timestamp
# current date and time
now = dt.datetime.now()

timestamp = dt.datetime.timestamp(now)
print("timestamp =", timestamp)

# sleep()
# The sleep() function suspends execution of the current thread for a given number of seconds.

import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")