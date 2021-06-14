from random import randint

def return_user_agent(file: str = "src/core/data/user-agents.txt") -> str:
    "Returns a random User-Agent"

    with open(file) as agents_file:

        user_agents = agents_file.readlines()
        user_agents = user_agents[randint(0, len(user_agents) -1)]
        user_agents = user_agents.encode('utf-8')

        return str(user_agents)