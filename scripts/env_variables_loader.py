"""
This module contains a function to load environment variables from a .env file.

The `load_envs` function takes a list of names of environment variables and returns their values.
It raises an exception if the .env file does not exist or if any of the specified variables are missing from the .env file.

If a .env.example file exists, it can load all .env.example varaibles. 

Outputs variables in dicts.
"""
import dotenv
import os
import sys


def load_environment_variables(env_variables: list[str]) -> dict[str, str]:
    """Loads environment variables from a .env file."""

    # Throw error if .env doesn't exist.
    if dotenv.load_dotenv(override=True) is False:
        raise FileNotFoundError(".env file not found.")

    environment_variables = {}

    # Check for variables
    for env_variable in env_variables:
        if os.getenv(env_variable) is None:
            raise KeyError(f"{env_variable} not found in .env file.")

        else:
            environment_variables[env_variable] = os.getenv(env_variable)

    return environment_variables


def load_all_environment_variables() -> dict[str, str]:
    """Loads all environment variables based on .env.example file."""

    # Throw error if .env.example doesn't exist.
    env_example_path = dotenv.find_dotenv(".env.example", raise_error_if_not_found=True)
    # Throw error if .env doesn't exist.
    if dotenv.load_dotenv(override=True) is False:
        raise FileNotFoundError(".env file not found.")

    # Read .env.example file.
    with open(env_example_path, "r") as env_example_file:
        env_example_variables = env_example_file.readlines()
        env_example_keys = [
            variable.split("=")[0] for variable in env_example_variables
        ]

    environment_variables = {}

    # Check for variables
    for env_example_key in env_example_keys:
        if os.getenv(env_example_key) is None:
            raise KeyError(f"{env_example_key} not found in .env file.")

        else:
            environment_variables[env_example_key] = os.getenv(env_example_key)

    return environment_variables
