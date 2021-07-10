from src.core.agent import user_agent


def get_file_data(path) -> str:
    with open(path) as file:
        return file.read('src/core/data/')


def get_urls() -> list:
    "Get all urls inside urls.txt file"

    raw = get_file_data('urls.txt')
    raw = raw.split('\n')
    return raw


def get_usernames() -> list:
    "Get all usernames inside usernames.txt file"

    raw = get_file_data('usernames.txt')
    raw = raw.split('\n')
    return raw


def get_passwords() -> list:
    "Get all passwords inside passwords.txt file"

    raw = get_file_data('passwords.txt')
    raw = raw.split('\n')
    return raw


headers = {'User-Agent': user_agent()}

props = {
    'verify': False,
    'timeout': 10,
    'allow_redirects': True,
    'headers': headers
}