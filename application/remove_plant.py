from infrastracture.storage import save_data

def remove_plant(plants, path, index):
    msg = "Успешно удалился"
    if 0 <= index < len(plants):
        plants.pop(index)
        save_data(path, plants)
    else:
        msg = "Такого растения не существует"

    return True, msg