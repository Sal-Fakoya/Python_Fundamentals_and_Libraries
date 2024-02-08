"""

                    TIME MODULE: perf_counter method
--> It is loaded from the time module
    --> from time import perf_counter
--> This is used to measure elapsed time in (float) seconds from an undefined start (0), which is usually when the
program starts running

--> perf_counter() is used for relative differences
--> It uses a clock with highest available precision

                    TIME MODULE: sleep method
-->  sleep(n) is used to pause execution for float (n) seconds
-->  Why would you want to slow your program down?
    --> Usually to give time for something else to finish, like an external resource like network connection or
    database by retrying connecting a few times, but wait-in between retries

                    GETTING THE EPOCH: using time.gmtime(n)
--> UNIX systems and modern UNIX systems use January 1, 1970 , 00:00:00 (UTC),
    --> by using time.gmtime(n) where:
            --> which is a time struct that returns a time object based on the epoch time n
            --> n is the number of seconds elapsed from epoch
            --> It ignores fractional seconds
--> To find the epoch on your system, pass zer (0)

                CURRENT EPOCH TIME: time.time()
--> Current epoch time is the time in the present
--> time.time() returns the current time in seconds since the epoch
--> time.gmtime(time.time()) returns the time struct in UTC

                CONVERTING FROM TIME_STRUCT TO EPOCH TIME: gmtime(n)
--> gmtime(n) converts an epoch time n to a time_struct

                CONVERTING EPOCH TIME TO STRUCT
--> We can also convert a time_struct back to an epoch time using the calendar module
--> calendar.timegm(time_struct) where:
        --> timegm is the inverse of gmtime
        --> It is located in the calendar module

            FORMATTING AN EPOCH TIME TO HUMAN READABLE STRING: strftime(format, time_struct)
--> If we show an epoch time (a float), that does not mean much to them
    --> As humans, we are used to certain formats for the date and time, hence to format date and time to human
    readable strings, use strftime(format, time_struct)

--> format directives include:
    --> %Y gives a four digit year
    --> %y gives a two digit year
    --> %m gives month number
    --> %B gives month full name
    --> %b gives months Abbreviated name
    --> %d is the day of the month number
    --> %H is the hour in 24-hour clock
    --> %I gives the hour in 12-hour clock
    --> %p is the AM or PM
    --> %M gives minute number
    --> %S gives second number
    --> %z gives time offset in +/- HHMM
    --> %Z gives a time zone name
    --> %w gives week day number
    --> %A gives weekday full name
    --> %a gives weekday abbreviated name

--> for instance, strftime("%Y-%m-%dT%H:%M:%Sz", t_struct)
                strftime("Today is %A, %B, %d %Y", t_struct)
                strftime("Time: %I:%M %p, %Z", t_struct)

                    PARSING DATE/TIME STRINGS: time.strptime(date_in_string, format)
--> The string parse time function is used to return a struct_time
--> Converting date strings to Epoch time, we use time.strptime() where:
            --> string parse time function which has 2 arguments for date in string and format we want to use to parse
            the string, e.g
            --> strptime(s, "%m/%d/%Y %I:%M:%S %p")
--> For every date/time formatting variant, we have to specify the format to parse it.
    e.g 4/18/2020 23:45:34 should be formatted as "%m/%d/%y %H:%M:%S"
        18/04/2020 11:45:34 PM should be formatted as "%d/%m/%Y %I:%M:%S %p"
        20/04/18 11:45:34 PM should be formatted as "%m/%d/%Y %I:%M:%S %p"
--> For data sources that use a mixture of formats. This is where a 3rd party library like dateutil can help
"""

import time
from time import strftime, gmtime, perf_counter, sleep
from calendar import timegm
import datetime

print(time.gmtime(0))

print(time.time())

print(time.gmtime(time.time()))

n = time.time()
t = time.gmtime(n)
print(timegm(t))

# USING perf_counter() as a timer
start = perf_counter()
end = perf_counter()
print(f'Elapsed = {end - start}')

# USING sleep(n) where n is in seconds
# start = perf_counter()
# sleep(3)
# end = perf_counter()
# print(f'Elapsed = {end-start}')

print(gmtime(1_000_000_000))

print(gmtime(0))

# print(gmtime(-1000000000))

# To print the current local time in UTC,
print(time.time())

# To print time.time() in epoch,
from time import time

print(gmtime(time()))


current = gmtime(time())

# Accessing contents of the struct by using indexes, attribute name and slicing
print(current[0])
print(current.tm_year)
print(current[0:2])

# Adding Two Days to the current time
now = time()
tomorrow = now + (24*60*60)
print(gmtime(now))
print(gmtime(tomorrow))

difference = tomorrow - now
print(gmtime(difference))

from calendar import timegm
now_epoch = time()

now_struct = gmtime(now_epoch)

print(timegm(now_struct))

now = gmtime(time())
from time import strftime, strptime

print(strftime('%Y/%m/%d', now))

print(strftime('%A is the best day of the week', now))

d = '12/11/10'
d1 = '2012-11-10'

print(strptime(d,"%y/%m/%d"))

print(strptime(d1,"%Y-%m-%d"))

s = "Monday, April 18, in the year 2020 CE"

fmt = "%A, %B %d, in the year %Y CE"

print(strptime(s, fmt))

s = "Monday, April 18, 2020"

# print(strptime(s, fmt)) will return error because the format designed does not match the date_string



