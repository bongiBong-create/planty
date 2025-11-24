def get_plants(plants):
    if len(plants) == 0:
        return True, "Список пуст"

    for i, value in enumerate(plants):
        print(f"Растение №{i + 1}\n"
              f"Имя: {value['name']}\n"
              f"Последний полив {value['date_last_watering']}"
              )

    return True, "Конец списка"