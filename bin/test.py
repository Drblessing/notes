#!/Users/dbless/Github/notes/bin/.bin_venv/bin/python
print("Hello World")

# Print which python version is being used
import sys

print(sys.version)

# Try and install a package
try:
    import requests

    print("requests is already installed")
except ImportError:
    print("requests is not installed, installing now")
    import subprocess

    subprocess.run(["pip", "install", "requests"])
    import requests
