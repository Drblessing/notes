import os
import json
import requests
import google.oauth2.id_token
import google.auth.transport.requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keyfile.json"
request = google.auth.transport.requests.Request()
audience = "https://<project_id>.cloudfunctions.net/function-3"
TOKEN = google.oauth2.id_token.fetch_id_token(request, audience)

r = requests.get(
    "https://<project_id>.cloudfunctions.net/function-3",
    headers={"Authorization": f"Bearer {TOKEN}"},
)
r.text
