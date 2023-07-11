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

# Other way to do it


from google.oauth2 import id_token
from google.oauth2 import service_account
import google.auth
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession

target_audience = "https://<project-id>.cloudfunctions.net/function-3"
url = "https://<project-id>.cloudfunctions.net/function-3"

creds = service_account.IDTokenCredentials.from_service_account_file(
    "keyfile.json", target_audience=target_audience
)

authed_session = AuthorizedSession(creds)

# make authenticated request and print the response, status_code
resp = authed_session.get(url)
print(resp.status_code)
print(resp.text)
