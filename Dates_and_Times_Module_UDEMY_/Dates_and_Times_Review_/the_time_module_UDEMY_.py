"""
                        PERF_COUNTER
--> perf_counter is used to measure elapsed time in (float) seconds
    --> from some undefined start (0) usually when the program starts running.
    --> always look at difference between calls to perf_counter
    --> uses clock with the highest available precision

                        SLEEP
--> sleep(n) is used to pause execution for float (n) seconds.
    --> to give time for something else to finish.
        --> usually some external resource or maybe a network connection is temporarily down
        --> We can re-try connecting a few times, but wait-in between tries.

                    GETTING THE EPOCH
--> UNIX systems use January 1, 1970, 00:00:00 (UTC)
--> time.gmtime(n) returns a time object (struct_time)
    --> based on n seconds elapsed from epoch
    --> has the following properties:
        --> tm_year, tm_mon, tm_day, tm_hour, tm_min, tm_sec and a few more
    --> ignores fractional seconds (if float)
--> time.gmtime(0) returns the epoch UTC struct_time object on your system

                        GETTING THE CURRENT EPOCH TIME
--> time.time() returns the current time (in seconds) since the epoch
--> time.gmtime(something_in_seconds) To get the UTC time_struct from a time in seconds, e.g
    --> e.g time.gmtime(time.time())

                        CONVERTING TIME_STRUCT TO EPOCH TIME
--> gmtime(some_epoch_time) converts an epoch time to a time_struct
--> calendar.timegm(time_struct) converts a time struct to epoch time
    --> timegm is the inverse of gmtime
    --> It is located in the calendar module:
        --> from calendar import timegm

                            FORMATTING EPOCH TIME TO A STRING:
--> strftime(format, time_struct) function (string format time)
    --> format is a string that contains special formatting directives

                                PARSING DATE AND TIME STRINGS
--> time.strptime(date_string, format)
    --> returns a struct time

NOTE: Know that time struct is a named tuple, where each element can be accessed using the .tm_something or with use
of index. You can even access multiple elements of the struct time by slicing.
"""
from time import perf_counter, sleep, gmtime, time, strftime, strptime
import time, calendar

start = perf_counter()
# some code here
end = perf_counter()
elapsed = end - start

print(elapsed)
#
# start = perf_counter()
# sleep(3)
# end = perf_counter()
# elapsed = end - start
# print(f'Elapsed time is {abs(elapsed)}')

epoch_in_sec = 1_000_000_000
epoch_to_struct = gmtime(epoch_in_sec)
print(epoch_to_struct)  # dst = 0 because UTC is doesn't use DST

epoch_in_sec = 0
epoch_t_to_struct = gmtime(epoch_in_sec)
print(epoch_t_to_struct)

# To check the current epoch in seconds on your system:
current_epoch_time = time.time()
current_epoch_time_in_struct = gmtime(current_epoch_time)

print(current_epoch_time)
print(current_epoch_time_in_struct)

current_year = current_epoch_time_in_struct.tm_year
print(current_year)
print(current_epoch_time_in_struct[0])

print(current_epoch_time_in_struct[0:2])

num_days = 1
num_days = 3600 * 24 * num_days

next2days_in_sec = time.time() + num_days
next2days_in_struct = gmtime(next2days_in_sec)
print(next2days_in_struct)

day_difference = next2days_in_sec - time.time()
print(day_difference)

# Time struct object in epoch. Need to import calendar module
now_struct = gmtime(time.time())  # have a struct time
now_epoch = calendar.timegm(now_struct)  # convert struct to epoch
print(now_epoch)

# TIME STRUCT to String: use strftime(format, time_struct)
now_struct = gmtime(time.time())
now_str = strftime('%Y/%m/%d', now_struct)
print(now_str)

some_text = strftime('%A is the best day of the week', now_struct)
print(some_text)  # Recall that the timezone is in UTC

# STRING TO TIME STRUCT: strptime(date_string, format)

# date_str = "12/11/10"
date_str1 = "2012-11-10"

date_struct = strptime(date_str1, '%Y-%m-%d')
print(date_struct)

s = 'Monday, April 18, in the year 2020 CE'
fmt = '%A, %B %d, in the year %Y CE'

s_to_struct = strptime(s, fmt)
print(s_to_struct)