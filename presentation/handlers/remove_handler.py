from application.remove_plant import remove_plant

def remove_handler(plants):
    try:
        index = int(input("Введите номер растения"))
        return remove_plant(plants, index - 1)
    except ValueError:
        print("Введите число!")

    return True