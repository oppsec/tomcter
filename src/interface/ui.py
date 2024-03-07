from rich.console import Console
console = Console()
from random import choice

def get_random_color() -> None:
    ''' Returns a random color from a predefined list '''
    
    color_list: list = [
        "cyan", "yellow", "red", "blue", "white", "magenta", "green",
        "italic cyan", "italic yellow", "italic red", "italic blue", "italic white", "italic magenta", "italic green",
        "bold cyan", "bold yellow", "bold red", "bold blue", "bold white", "bold magenta", "bold green",
    ]
    
    return choice(color_list)

def get_banner() -> None:
    """ Return the content from banner.txt as application banner """

    ascii = """
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|     Tomcter 0.8
    `-.-' \ )-`( , o o)     Stealing credentials from the yellow cat
          `-    \`_`"'-

"""
    console.print(f"[{get_random_color()}]{ascii}[/]")