from presentation.config import cmd_add, cmd_remove, cmd_plant, cmd_out
from presentation.handlers.add_handler import add_handler
from presentation.handlers.remove_handler import remove_handler
from presentation.handlers.get_handler import get_handler
from presentation.handlers.out_handler import out_handler

plants = []

def start_cli():
    print("Planty!")

    commands = {
        cmd_add: add_handler,
        cmd_remove: remove_handler,
        cmd_plant: get_handler,
        cmd_out: out_handler
    }

    flag = True

    while flag:
        command = input(f"Введите команду: {"/".join(commands.keys())}\n")
        handler = commands.get(command)

        if handler:
            flag, msg = handler(plants)
            print(msg)
        else:
            print("Введите корректную команду")