from rich import print

def banner() -> str:
    """ Return the content from banner.txt as application banner """

    file: str = "src/interface/banner.txt"

    with open(file) as banner_file:
        content = banner_file.read()

        print(f"[yellow][b]{content}[/][/]")