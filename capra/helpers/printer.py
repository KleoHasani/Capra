from termcolor import colored
from capra.helpers.globals import OutType, CWP


def banner() -> None:
    title = """
     ▄████▄   ▄▄▄       ██▓███   ██▀███   ▄▄▄      
    ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓██ ▒ ██▒▒████▄    
    ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▓██ ░▄█ ▒▒██  ▀█▄  
    ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▀▀█▄  ░██▄▄▄▄██ 
    ▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░██▓ ▒██▒ ▓█   ▓██▒
    ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
    ░  ▒     ▒   ▒▒ ░░▒ ░       ░▒ ░ ▒░  ▒   ▒▒ ░
    ░          ░   ▒   ░░         ░░   ░   ░   ▒   
    ░ ░            ░  ░            ░           ░  ░
    ░                                              
    """
    author = "Made with 💖 by Kleo Hasani"
    github = "https://github.com/KleoHasani/Capra"

    print(colored(title, color="red"))
    print(f'{" " * 12}{colored(author, color="blue")}\n')
    print(f'{colored("GitHub", color="yellow")} \t›\t{github}\n')

    pass


def cinput(chr: str = "λ ") -> str:
    print(f'╭─[{colored(CWP, color="blue")}]')
    return input(f'╰─{colored(chr, color="green")}')


def output(msg: str, type: OutType = OutType.WARNING) -> None:
    print("\n", colored(f"[{type.name}]", color=type.value), msg, "\n")
    pass


def done(msg: str = "") -> None:
    print(
        f'\n{colored("[Done]", color="green")}\t {colored(msg, color="yellow")}\n'
    )
    pass


def menu(title: str, options: dict[str, str]) -> None:
    print("\n\n", colored(title, color="cyan"), "\n")
    for opt, msg in options.items():
        print(colored(opt, color="green"), "\t", msg)
    print("\n")
    pass
