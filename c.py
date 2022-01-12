import package1.a
import sys
import requests

response = requests.get("https://randomuser.me/api")

data = response.json()


print(len(data))

for user in data["results"]:
    print(user)


print(2)
