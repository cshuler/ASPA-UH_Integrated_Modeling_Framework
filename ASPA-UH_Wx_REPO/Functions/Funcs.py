#This is the make-a-list-of-consecutive-dates function
from datetime import date, datetime, timedelta
def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current < end:
        yield current
        current += delta