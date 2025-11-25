from application.add_plant import add_plant
from shared.validators import validation_int, validation_datetime

def add_handler(plants, path):
    name = input("Введите имя растения\n")
    type_plant = input("Введите тип растения\n")
    interval = input("Введите интервал полива\n")

    if not validation_int(interval):
        return True, "Введите число"

    date_last_watering = input("Введите дату последнего полива в формате дд.мм.гггг\n")

    if not validation_datetime(date_last_watering):
        return True, "Введите корректную дату"

    return add_plant(plants, path, name, type_plant, date_last_watering, interval)
