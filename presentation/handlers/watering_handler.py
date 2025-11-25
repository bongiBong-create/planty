from application.watering_plant import watering_plant

def watering_handler(plants, path):
    try:
        index = int(input("Введите номер растения\n"))
        return watering_plant(plants, path, index - 1)
    except ValueError:
        print("Введите число")
        return True, "Введите корректный номер растения"