from shared.create_id import create_id

def add_plant(plants, name, type_plant, date_last_watering, interval):
    plant = {"id": create_id(),
             "name": name, "type_plant": type_plant,
             "date_last_watering": date_last_watering,
             "interval": interval}

    plants.append(plant)

    return True, f"{name} успешно добавлено"