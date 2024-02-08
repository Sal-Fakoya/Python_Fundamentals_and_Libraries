"""
                            CUSTOM DATE REPRESENTATIONS
--> Recall time module:
    --> strftime(some_format, time_struct) used to format time_struct using the formatting directives
    --> strptime(date_string, format) used to parse a date string into a struct

--> strftime is also available for:
    --> datetime.time
    --> datetime.date
    --> datetime.datetime
--> strptime is ONLY available for datetime.datetime objects.

"""

from datetime import date, time, datetime, timedelta, timezone

t = time(22, 30, 45)

ans = t.strftime('The time is %I hours, %M minutes and %S seconds, %p')
print(ans)

d = date(2020, 5, 15)
print(d.strftime('%x'))

dt = datetime(2020, 5, 15, 22, 30, 45)

print(dt.strftime('%I:%M %p on %B %d, %Y'))

dt = datetime.strptime('10:30 PM on May 15, 2020', '%I:%M %p on %B %d, %Y')
print(dt)

dt_iso_formatstr = dt.isoformat()

print(dt_iso_formatstr)

dt_iso_formatted = datetime.fromisoformat(dt_iso_formatstr)
print(dt_iso_formatted)

print(dt_iso_formatted.tzinfo)

dt_aware = dt_iso_formatted.replace(tzinfo=timezone.utc)
print(dt_aware)
print(dt_aware.tzinfo)

dt_iso_formatted = datetime.fromisoformat('2020-05-15 22:30:00-05:00')





