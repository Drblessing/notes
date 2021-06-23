# Simple script to manage your API keys in a .env file

import os  # Handles getting env variables
import dotenv  # Handles .env

# load .env file
dotenv.load_dotenv()


def api_key(name: str) -> str:
    return os.getenv(name)


if __name__ == "__main__":
    TEST_API_KEY = api_key("TEST_API_KEY")

    print(TEST_API_KEY)