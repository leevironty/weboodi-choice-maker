from datetimerange import DateTimeRange
import datetime
from dateutil.relativedelta import relativedelta
from typing import List


def get_event_list(s: str, n = 10, start_date: datetime.date = None) -> List[DateTimeRange]:
    """Input string sould be of form '<weekday> <start time>-<end time>'"""
    weekdays = ["ma", "ti", "ke", "to", "pe", "la", "su"]
    weekday, time = s.split(" ")  # TODO: add input sanitization
    weekday = weekdays.index(weekday) + 1
    time_start, time_end = get_deltas(time)
    if start_date is None:
        start_date = next_weekday_after_date(datetime.date.today(), weekday)
    return get_n_events(start_date, time_start, time_end, n)

def get_deltas(time_string: str) -> (relativedelta, relativedelta):
    """time_string: '<hours>.<minutes>-<hours>.<minutes>"""
    t1, t2 = time_string.split("-")
    time_start = get_delta(t1)
    time_end = get_delta(t2)
    return time_start, time_end

def get_delta(time_string: str) -> relativedelta:
    """time_string: '<hours>.<minutes>'"""
    h, m = time_string.split(".")
    return relativedelta(hours=int(h), minutes=int(m))

def next_weekday_after_date(date: datetime.date, weekday: int) -> datetime.date:
    d = relativedelta(days=1)
    for i in range(7):
        day = date + i*d
        if day.isoweekday() == weekday:
            return day
    raise IndexError("This should never happen")


def get_n_events(first_date: datetime.date, start_time: relativedelta, end_time: relativedelta, n: int) -> List[DateTimeRange]:
    week = relativedelta(days=7)
    date_range_list = []
    for i in range(n):
        d = first_date + i*week
        date_range_list.append(DateTimeRange(d+start_time, d + end_time))
    return date_range_list
