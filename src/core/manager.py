from random import randint

def get_file_data(path) -> str:
    " Return the content inside text file "

    with open(path) as file:
        return file.read()


def get_usernames() -> list:
    " Get all usernames inside usernames.txt file "

    raw = get_file_data('src/core/data/usernames.txt')
    raw = raw.split('\n')
    return raw


def get_passwords() -> list:
    " Get all passwords inside passwords.txt file "

    raw = get_file_data('src/core/data/passwords.txt')
    raw = raw.split('\n')
    return raw


def user_agent() -> str:
    """  Return a random user-agent from user-agents.txt file """

    user_agents_file: str = "src/core/data/user-agents.txt"

    with open(user_agents_file, 'r+') as user_agents:
        user_agent = user_agents.readlines()
        user_agent = user_agent[randint(0, len(user_agent) -1)]
        user_agent = user_agent.encode('utf-8')

        return str(user_agent)


headers = {'User-Agent': user_agent()}

props = {
    "verify": False,
    "timeout": 25,
    "allow_redirects": True,
    "headers": headers
}