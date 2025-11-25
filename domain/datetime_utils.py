from domain.config import formatted
from datetime import datetime, timedelta

def today_datetime():
    return datetime.today().date()

def parse_datetime(date):
    return datetime.strptime(date, formatted).date()

def format_datetime(date):
    return date.strftime(formatted)

def datetime_next_watering(date_last_watering, interval):
        return date_last_watering + timedelta(days=interval)

def needs_watering(today_date, next_date):
    return today_date >= next_date