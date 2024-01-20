DOT_ENV_PATH = ".env"


# def parse_dot_env():
#     env_vars = {}
#     try:
#         with open(DOT_ENV_PATH, "r") as file:
#             for line in file:
#                 line = line.strip()
#                 if line and not line.startswith("#"):
#                     key, value = line.split("=", 1)
#                     env_vars[key] = value
#     except FileNotFoundError:
#         return env_vars
#     return env_vars


def parse_dot_env():
    env_vars = {}
    try:
        with open(DOT_ENV_PATH) as file:
            env_vars = {
                key: value
                for line in file
                if (line := line.strip()) and not line.startswith("#")
                for key, value in [line.split("=", 1)]
            }
    except FileNotFoundError:
        pass
    return env_vars
