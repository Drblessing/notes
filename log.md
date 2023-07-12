# 2023-07-12

## Python load envs boilerplate

```python
def load_envs(*names) -> list:
    import os
    import dotenv

    dotenv.load_dotenv()

    if len(names) == 1 and isinstance(names[0], list):
        names = names[0]

    return [os.getenv(name, "") for name in names]
```

Works with list or multiple arguments.

# 2023-07-11

## Running authenticated google cloud functions

Okay this was actually a struggle, because the documentation is not very clear on how to do this. The key for me was the audience parameter.

I will write a full blog post on this, but for now here is the gist of it.

1. Create a service account with the correct permissions, cloud invoker, and run invoker for v2 functions.

2. Create a keyfile.json for the service account and download it.

3. Fetch the id token using the google oauth2 library, after linking the keyfile.json to the GOOGLE_APPLICATION_CREDENTIALS environment variable.

```python
import os
import json
import requests
import google.oauth2.id_token
import google.auth.transport.requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keyfile.json"
request = google.auth.transport.requests.Request()
audience = "https://<projectid>.cloudfunctions.net/function-3"
TOKEN = google.oauth2.id_token.fetch_id_token(request, audience)

r = requests.get(
    "https://<projectid>.cloudfunctions.net/function-3",
    headers={"Authorization": f"Bearer {TOKEN}"},
)
r.text
```

More in [gcloud_functions.py](scripts/gcloud_functions.py)

4. To do it with the authenticated request session, you need to create a authenticated reqeust session.

## Creating Google Cloud Function

You can use the cli but you can also upload a zip file with the code and requirements.txt. Needs to use functions frameworks and main.py.

## Adding pip dependencies to AWS lambda functions

This is also a pain, you can't just have it install from a requirements.txt, you need to either add the depenedencies as a layer, or zip the dependencies with the function. For C-dependent packages, you have to use layers. You can also create a Docker image of the function and deploy it that way.

## Hosting simple python apps

AWS Lambda or Google CLoud Functions have generous free tiers.

If you use Docker, use AWS Lambda, because you can create a Docker image and deploy it to AWS Lambda.

## Deploying Docker images to AWS Lambda

https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions

The main part is you have to export access keys from aws that have ecr permissions, and then use the aws cli to login to docker.

Login to docker:

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 111111111.dkr.ecr.us-east-1.amazonaws.com`

Build the image:

`docker tag docker-image:test 111111111.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest`

Push the image:

`docker push 111111111.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest`

Replace 111111111 with your account id, and hello-world with the name of your image, and Amazon ECR repository URI with the repositoryURI of your ECR repository.
