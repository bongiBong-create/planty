def print_watering_plants(check_plants):
    if check_plants:
        print("Нужно полить эти растения:")
        for plant in check_plants:
            print(f"{plant['name']} (прошлый полив был: {plant['date_last_watering']})\n")
    else:
        print("Поливать нечего")