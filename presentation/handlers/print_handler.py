from application.get_plants import get_plants

def print_handler(plants, path):
    plants = get_plants(plants)

    if not plants:
        return True, "Список пуст"

    for i, value in enumerate(plants):
        print(f"Растение №{i + 1}\n"
              f"Имя: {value['name']}\n"
              f"Последний полив: {value['date_last_watering']}\n"
              f"Следующий полив: {value['date_next_watering']}\n"
              )

    return True, "Конец списка"