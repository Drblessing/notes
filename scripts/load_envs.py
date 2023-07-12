def load_envs(*names) -> list:
    import os
    import dotenv

    dotenv.load_dotenv()

    if len(names) == 1 and isinstance(names[0], list):
        names = names[0]

    return [os.getenv(name, "") for name in names]