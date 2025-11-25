from domain.datetime_utils import parse_datetime

def validation_int(num):
    try:
        return int(num)
    except ValueError:
        return False

def validation_datetime(date):
    try:
         return parse_datetime(date)
    except ValueError:
        return False