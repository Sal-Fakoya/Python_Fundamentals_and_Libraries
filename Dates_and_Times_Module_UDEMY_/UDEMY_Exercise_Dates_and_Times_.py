# QUESTION 1
"""
Write a function that, given an epoch timestamp, returns a `datetime`
object set to the beginning of that month (so midnight of the first day
of the month).
"""
import datetime
from datetime import time, timedelta
import time

def epoch_to_datetime(epoch_time):
    epoch_struct = time.gmtime(epoch_time)
    return datetime.datetime(epoch_struct.tm_year, epoch_struct.tm_mon, 1, 0, 0)


epoch_time = float(input('Enter time in seconds: '))
print(epoch_to_datetime(epoch_time))

"""
QUESTION 2
Write a function that returns the difference in hours between two dates provided as Python
standard ISO formatted strings, rounded to the nearest hour. For simplicity, assume that these dates
do not contain fractional seconds.

For example, given these two string dates:
```
2001-01-01T13:50:23
```

and 
```
2001-06-12T14:23:50
```

your result should be `3889` hours.
"""

date1 = '2001-01-01T13:50:23'
# input('Enter first date: ')
date2 = '2001-06-12T14:23:50'
# input('Enter second date: ')

date_list = (datetime.datetime.fromisoformat(each_date)
             for each_date in [date2, date1])

date_diff = next(date_list) - next(date_list)
date_diff = int(date_diff.total_seconds())
date_diff = round(date_diff // (60 * 60))

print(f'The total hours are {date_diff}')

# QUESTION 3
"""
Write a function that can be used to consistently format `datetime` 
objects into strings with some default format, 
but allows the caller to override the default format.

For example, the default format could be `mm/dd/yyyy hh:mm:ss am/pm`, but your function 
allows itself to be called with some argument that can override that format.
"""


def datetime_to_strformat(datetime_obj, strformat='%m/%d/%Y %I:%M:%S %p'):
    datetime_obj = datetime_obj.strftime(strformat)
    return datetime_obj


print(datetime_to_strformat(datetime.datetime(2020, 12, 5)))

