import os
from capra.globals import HELP_MENU
from capra.io import banner, menu, cinput


class InvalidInputException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Application:
    def __init__(self) -> None:
        banner()
        pass

    def start(self) -> None:
        while True:
            inp: str = cinput()

            if inp == "exit":
                break

            elif inp == "help":
                menu("Help Menu", HELP_MENU)

            elif inp == "clear":
                os.system("clear")

            elif inp == "banner":
                os.system("clear")
                banner()

            elif inp == "config":
                # Set application config.
                pass

            else:
                raise InvalidInputException(f"Invalid input '{inp}'")
        pass
