from application.add_plant import add_plant

def add_handler(plants):
    name = input("Введите имя растения\n")
    type_plant = input("Введите тип растения\n")
    date_last_watering = input("Введите дату последнего полива в формате дд.мм.гггг\n")
    interval = input("Введите интервал полива\n")

    return add_plant(plants, name, type_plant, date_last_watering, interval)
