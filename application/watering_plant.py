from domain.watering_service import updated_watering
from domain.datetime_utils import format_datetime
from infrastracture.storage import save_data

def watering_plant(plants, path, index):
    if 0 <= index < len(plants):
        plant = plants[index]
        today_watering, next_watering = updated_watering(plant['interval'])
        plant['date_last_watering'] = format_datetime(today_watering)
        plant['date_next_watering'] = format_datetime(next_watering)

        save_data(path, plants)
        return True, "Полит"

    return True, "Такого растения не существует"