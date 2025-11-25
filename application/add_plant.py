from shared.create_id import create_id
from infrastracture.storage import save_data
from domain.datetime_utils import datetime_next_watering, format_datetime
from shared.validators import validation_datetime,validation_int

def add_plant(plants, path, name, type_plant, date_last_watering, interval):
    valid_datetime = validation_datetime(date_last_watering)
    valid_interval = validation_int(interval)

    if not valid_datetime:
        return True, "Введите корректную дату"

    if not valid_interval:
        return True, "Введите число"

    date_next_watering = format_datetime(datetime_next_watering(valid_datetime, valid_interval))

    plant = {"id": create_id(),
             "name": name,
             "type_plant": type_plant,
             "date_last_watering": date_last_watering,
             "date_next_watering": date_next_watering,
             "interval": interval}

    plants.append(plant)
    save_data(path, plants)

    return True, "Зеленый успешно добавлен"