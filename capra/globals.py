import os
from enum import Enum


CWP: str = os.getcwd()


HELP_MENU: dict[str, str] = {
    "help": "Show this help menu.",
    "clear": "Clear terminal output.",
    "banner": "Show application banner.",
    "config": "Set global application configuration",
    "exit": "Close the application.",
}


class OutType(Enum):
    WARNING = "yellow"
    ERROR = "red"
