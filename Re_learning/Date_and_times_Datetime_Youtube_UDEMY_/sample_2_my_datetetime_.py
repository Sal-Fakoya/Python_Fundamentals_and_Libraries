# Dates
import datetime
import pytz

my_date = datetime.date(2018, 12, 16)
print(my_date)
print(type(my_date))

my_date_str = str(my_date)
print(type(my_date_str))

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)

print(tday.year)
print(tday.day)

tday_week = tday.isoweekday()
print(tday_week)
# Monday = 1, Sunday == 7

tday_week = tday.weekday()
print(tday_week)
# Monday == 0, Sunday == 6

# TIMEDELTA: is the difference between two days and/or times and are useful when we want to perform operation and
# dates and times. It has methods like total seconds, days,
tdelta = datetime.timedelta(days=7)
tday_plus_7days = tday + tdelta
print(tday_plus_7days)

tdelta = datetime.timedelta(hours=7)
tday_plus_7days = tday + tdelta
print(tday_plus_7days)

tday_minus_7days = tday - tdelta
print(tday_minus_7days)

tdelta1 = tday_plus_7days - tday
print(tdelta1)

tdelta2 = tday - tday_minus_7days
print(tdelta2)

bday = datetime.date(2024, 7, 8)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

# TIME: .time allows us to work with time. By default doesn't have timezone information, but tzinfo that can be
# specified
t = datetime.time(9, 30, 45, 100_000)
print(t.hour)

# DATETIME: .datetime allows us to work with dates and times. By default, doesn't have tzinfo, but tzinfo can be
# specified

t = datetime.datetime(2016, 7, 26, 12, 30, 45, 100_000)
print(t.date())
print(t.weekday())
print(t.isoweekday())
print(t.year)
print(t.second)
print(t)

t1 = datetime.datetime(2016, 7, 26, 12, 30, 45, 100_000, pytz.timezone('America/Chicago'))
print(t1)

chic_tz = pytz.timezone('America/Chicago')
t1 = datetime.datetime(2016, 7, 26, 12, 30, 45, 100_000, chic_tz)
print(t1)

t2 = datetime.datetime(2016, 7, 26, 12, 30, 45, 100_000)
print(t2)
t2 = t2.astimezone(chic_tz)
print(t2)

east_tz = pytz.timezone('US/Eastern')
tday = datetime.datetime.today()
tday_with_timezone = tday.astimezone(east_tz)
print(tday_with_timezone)

tdelta = datetime.timedelta(days=7)
tdelta_plus_tday = tdelta + tday
print(tdelta_plus_tday)

my_tdelta = datetime.timedelta(hours=12)
tdelta_plus_tday_hours = my_tdelta + tday
print(tdelta_plus_tday_hours)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

chic_tz2 = pytz.timezone('America/Chicago')
tday = datetime.datetime.today()
tday_with_timezone = tday.astimezone(chic_tz2)
print(tday_with_timezone)

tnow_with_timezone = datetime.datetime.now(chic_tz)
# tday_with_timezone = tday.astimezone(chic_tz2)
print(tnow_with_timezone)

# Difference between .now() and .today(): .today() returns current local datetime with timezone of now
# and .now() gives the option to pass timezone as an argument

# .utcnow() gives us the current utc time, but the tzinfo is set to None
# .utcnow().replace(tzinfo=pytz.utc) creates the current utc time that is timezone aware
# pytz.utc allows us to create a timezone aware time on datetime.datetime objects except datetime.datetime.today()
#  astimezone allows us to convert timezones

t3_aware = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.utc)
print(t3_aware)

dt_now_aware = datetime.datetime.now(tz=pytz.utc)
print(dt_now_aware)

east_tz = pytz.timezone('US/Eastern')

tday_naive = datetime.datetime.today()
tday_with_timezone = tday_naive.astimezone(east_tz)
print(tday_with_timezone)

dt_now_aware = datetime.datetime.now(pytz.utc)
dt_east1 = dt_now_aware.astimezone(east_tz)
print(dt_east1)

chic_tz = pytz.timezone('America/Chicago')
tday_aware = chic_tz.localize(tday_naive)

dt_east3 = east_tz.localize(tday_naive)
print(dt_east3)

dt_east2 = tday_aware.astimezone(east_tz)
print(dt_east2)

# It is critical to always convert datetime.datetime.now() and datetime.datetime.today() into aware datetime objects
# when working with them in case you ever need to convert to another timezone.

"""
You can localize/change naive objects to aware objects by using .localize() method.

For datetime.datetime.now() and datetime.datetime.today(), You can localize them to another timezone by:
    --> some_timezone.localize(naive_object)

However, localizing datetime.datetime.utcnow() will require to use:
    --> utc_aware_variable = pytz.utc.localize(naive_utcnow).

utcnow() object is a standard and fixed timezone, therefore it does not accept any timezone argument. So, it can only be
    localized using pytz.utc.localize(naive_utc_now) or naive_utc_now.replace(pytz.utc)
    
    DO NOT/NEVER use a timezone to localize a utc now object, e.g never do this:
    east_tz = pytz.timezone('US/Eastern')
    utc_now_aware = east_tz.localize(naive_utc_now)     
    
    Now, the utcnow() object which is already made aware can be 
    converted to another timezone using utcnow_aware_object.astimezone(some_ptyz.timezone('time_zone_in_str'))

"""


print()

chic_tz = pytz.timezone('America/Chicago')
chic_tz_aware = chic_tz.localize(datetime.datetime.now())
print(chic_tz_aware)

# To save/pass datetime objects for internal use,
print(chic_tz_aware.isoformat())

# Datetime to strimg
datetime_to_str = chic_tz_aware.strftime("%B  %d, %Y")
print(datetime_to_str)

# String to Datetime
str_datetime = "December  16, 2023"
str_to_datetime = datetime.datetime.strptime(str_datetime, "%B  %d, %Y")

print(str_to_datetime)








