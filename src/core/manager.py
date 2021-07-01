from src.core.agent import get_user_agent

def get_file_data(path) -> None:
    with open(path) as file:
        return file.read()


def get_urls() -> list:
    "Get all URLS inside urls.txt"

    raw = get_file_data('src/core/data/urls.txt')
    raw = raw.split('\n')
    return raw


def get_usernames() -> list:
    "Get all USERNAMES inside usernames.txt"

    raw = get_file_data('src/core/data/usernames.txt')
    raw = raw.split('\n')
    return raw


def get_passwords() -> list:
    "Get all PASSWORDS inside passwords.txt"

    raw = get_file_data('src/core/data/passwords.txt')
    raw = raw.split('\n')
    return raw


headers = {'User-Agent': get_user_agent()}

props = {
    'verify': False,
    'timeout': 10,
    'allow_redirects': True,
    'headers': headers
}