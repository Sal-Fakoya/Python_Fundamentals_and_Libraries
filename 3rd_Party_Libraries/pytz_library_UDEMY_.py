"""
                THE PYTZ LIBRARY
--> Pytz is used for dealing with timezones
--> It implements the Olson (IANA) Database
--> It supports DST
--> Provides a uniform naming convention e.g
    --> US/Eastern
    --> America/New York
    --> Europe/Paris
    Goes by Area/Location
--> In terms of calculation, goes back to 1970.

                        PYTZ FUNCTIONALITY
--> pytz.all_timezones returns a list of all named timezones.
--> It internally uses python's tzinfo but with some extras for DST
--> A pytz timezone can be used instead of a tzinfo object.

                    LOOKING UP A TIMEZONE
--> We can retrieve a timezone from its name:
    --> using pytz.timezone(timezone_info_in_str)
    --> pytz.timezone('utc') or pytz.utc to get utc timezone
--> We can use pytz.timezone(some_timezone_str) instead of Python's tzinfo:
    e.g datetime.datetime(
                        2020, 5, 15, 10, 0, 0, tzinfo=pytz.timezone('US/Eastern')
                        )  #datetime aware time

                    MAKING A NAIVE DATETIME AWARE
--> We use pytz time zone's "localize" method e.g:
    --> tz_NY = pytz.timezone('America/New_York')
    --> tz_aware = tz_NY.localize(some_naive_datetime_obj)
--> Note that pytz will figure out whether to use DST or not. You don't need to worry about specifying anything for DST.
--> Using the localize method attaches the timezone information to the naive datetime, it does not convert the
datetime to new timezone.

                        CONVERTING AWARE DATETIME TO OTHER TIMEZONES: astimezone(new_time_zone) method:
--> Once we have an aware datetime, we can convert it to another timezone.
    --> By using the some_aware_dt.astimezone(new_timezone)
--> If we start with a naive time, we must make it aware in UTC first using .localize() before using as timezone
--> If we start with a naive UTC time, we can directly transform it to a specific timezone using fromutc method.
    --> some_pytz_timezone.fromutc(naive_utc_datetime)
"""

import pytz
from datetime import datetime, timezone

for tz in pytz.all_timezones:
    print(tz)

tz_chicago = pytz.timezone('America/Chicago')
print(tz_chicago)
print(type(tz_chicago))

# Getting UTC timezone
tz_utc = pytz.utc
print(tz_utc)
# OR
tz_utc1 = pytz.timezone('UTC')
print(tz_utc1)

print(tz_utc.zone)
print(tz_chicago.zone)

dt_naive = datetime(2020, 5, 15, 10, 0, 0)
print(dt_naive.tzinfo)

dt_chicago = tz_chicago.localize(dt_naive)  # adjusted for DST
print(dt_chicago)

dt_chicago = dt_naive.replace(tzinfo=tz_chicago)
print(dt_chicago)  # not adjusted for  DST

print(tz_chicago.localize(datetime(2019, 12, 31, 10, 0, 0)))

tz_melbourne = pytz.timezone('Australia/Melbourne')
chicago_to_melbourne = dt_chicago.astimezone(tz_melbourne)
print(chicago_to_melbourne)

print(dt_chicago.astimezone(pytz.utc))

dt_utc_naive = datetime.utcnow()
print(dt_utc_naive)

# Converting a naive UTC to aware UTC
dt_utc_aware = pytz.utc.localize(dt_utc_naive)
print(dt_utc_aware)

# OR
dt_utc_aware = datetime.utcnow().replace(tzinfo=pytz.utc)
print(dt_utc_aware)

print(dt_utc_aware.astimezone(tz_melbourne))

dt_utc_aware.astimezone(tz_chicago)

now_utc = dt_utc_aware

# converting naive utc directly to another timezone using .fromutc() method
dtfromutc_to_chicago = tz_chicago.fromutc(dt_utc_naive)
print(dtfromutc_to_chicago)
