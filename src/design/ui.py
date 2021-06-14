from rich import print
from os import system, name


def get_banner(file_name: str = "src/design/banner.txt") -> str:
    with open(file_name) as banner_file:
        file_content = banner_file.read()

        print(f"[yellow][b]{file_content}[/][/]")


def clear() -> None:
    system('cls' if name == 'nt ' else 'clear')