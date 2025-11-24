def remove_plant(plants, index):
    msg = "Успешно удалился"
    if 0 <= index < len(plants):
        plants.pop(index)
    else:
        msg = "Такого растения не существует"

    return True, msg