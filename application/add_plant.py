from infrastracture.storage import save_data
from shared.create_id import create_id

def add_plant(plants, path, name, type_plant, date_last_watering, interval):
    plant = {"id": create_id(),
             "name": name, "type_plant": type_plant,
             "date_last_watering": date_last_watering,
             "interval": interval}

    plants.append(plant)
    save_data(path, plants)

    return True, f"Зеленый успешно добавлен"