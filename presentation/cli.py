from infrastracture.storage import init_path, init_storage, get_data
from presentation.config import cmd_add, cmd_remove, cmd_plant, cmd_out, cmd_watering
from presentation.handlers.add_handler import add_handler
from presentation.handlers.remove_handler import remove_handler
from presentation.handlers.print_handler import print_handler
from presentation.handlers.out_handler import out_handler
from presentation.handlers.watering_handler import watering_handler
from presentation.handlers.print_watering_plants import print_watering_plants
from domain.watering_service import check_watering

def start_cli():
    print("Planty!")
    path = init_path()
    init_storage(path)
    plants = get_data(path)

    commands = {
        cmd_add: add_handler,
        cmd_remove: remove_handler,
        cmd_plant: print_handler,
        cmd_out: out_handler,
        cmd_watering: watering_handler
    }

    check_plants = check_watering(plants)
    print("Проверяем, кого нужно полить...")
    print_watering_plants(check_plants)

    flag = True

    while flag:
        command = input(f"Введите команду: {"/".join(commands.keys())}\n")
        handler = commands.get(command)

        if handler:
            flag, msg = handler(plants, path)
            print(msg)
        else:
            print("Введите корректную команду")