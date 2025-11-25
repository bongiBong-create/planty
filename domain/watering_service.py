from domain.datetime_utils import today_datetime, parse_datetime, datetime_next_watering

def check_watering(plants):
    today = today_datetime()

    check_plants = [plant for plant in plants if parse_datetime(plant['date_next_watering']) <= today]

    return check_plants

def updated_watering(interval):
    today_watering = today_datetime()
    next_watering = datetime_next_watering(today_watering, interval)
    return today_watering, next_watering