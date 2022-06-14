import os
from os.path import join
from pathlib import Path
from enum import Enum


CWP: str = os.getcwd()
HOME: str = Path.home()
CONFIG_PATH: str = join(HOME, ".capra")
LOG_PATH: str = join(HOME, ".capra_log")

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
