from application.remove_plant import remove_plant

def remove_handler(plants, path):
    try:
        index = int(input("Введите номер растения\n"))
        return remove_plant(plants, path, index - 1)
    except ValueError:
        print("Введите число!")

    return True