from rich import print
from os import system, name


def banner() -> str:
    """ Returns the application banner
    """

    file: str = "src/design/banner.txt"

    with open(file) as banner_file:
        content = banner_file.read()

        print(f"[yellow][b]{content}[/][/]")


def clear() -> None:
    """ Clear the screen
    """

    system('cls' if name == 'nt' else 'clear')