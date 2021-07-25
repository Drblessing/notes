# Utils

## Python quickstart 

[Install anaconda](https://www.anaconda.com/products/individual)

#### Upgrading base env

On your terminal, run:

```shell
$ conda update anaconda
$ conda update python
$ pip install --upgrade pip
```

Creating and activating venv:

```shell
$ virtualenv --python=$pythonversion $name
$ source $name/bin/activate
```

#### Dependency management

Building dependency list:

```shell
$ pip install pip-chill
$ pip-chill > requirements.txt
```
Or, if you want it without version numbers:

```shell
$ pip-chill --no-version > requirements.txt
```

Installing dependencies: 

```shell
$ pip install -r requirements.txt
```

## Website quickstart

Create a new env and install packages:

```shell
$ pip install -r website_requirements.txt
```

Code your app.

Add [Google analytics](https://analytics.google.com/), here's an [example script](ga.html).

Put this at the start of your html templates:

```html
{% block head %}
{{ super() }}
{% include "ga.html" %}
{% endblock %}
```
Deploy flask directly to [aws elastic beanstalk](https://aws.amazon.com/elasticbeanstalk/), [pythonanywhere](https://www.pythonanywhere.com/), or [more options here](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html). 

Or, build a [Docker image](Dockerfile), and deploy to [aws elastic beanstalk](https://aws.amazon.com/elasticbeanstalk/) or [more options here](https://geekflare.com/docker-hosting-platforms/).

### [Elastic Beanstalk Deployment](https://console.aws.amazon.com/elasticbeanstalk)

#### Upload and Deploy

Manually zip your files with no parent directory and upload directly to eb environments in your applications.

For Flask envs, elastic beanstalk searches launches from `application` flask object in the root directory.

For Docker envs, elastic beanstalk searchers launches from `Dockerfile` and `Dockerrun.aws.json` in the root directory. Implement a WSGI.

#### [EB CLI](https://github.com/aws/aws-elastic-beanstalk-cli-setup)

For big brains, manage eb from the command line. 

Build a `deploy.sh` script and requires a `docker-compose.yaml` file.  

#### Other Deployment methods

You can also deploy environments from s3 buckets or private/public Docker repositories. 

### Elastic Beanstalk Configuration  

Environments > Configuration on sidebar 

To manage maximum scaling up, edit the max field in capacity. If you set max to 1 you can limit potential max cost. 
For cores per instance, check [here](https://aws.amazon.com/ec2/physicalcores/). For gunicorn, roughly # workers = # cores * 2 + 1

#### Better Domain

For last-minute maximal convenience, purchase a domain from Amazon Route 53 [here](https://console.aws.amazon.com/route53/v2).

`.io` domains are in vogue now. 

If you're creating a crypto rugpull, consider a `.finance` domain. 

To point your new shiny domain name to your eb environment: 

- Go to AWS Route 53 > Hosted Zone > Clock domain name
- Create Record > Wizard Create > Simple Routing 
- Define Simple Record > Value/Route Traffic to > Alias to Elastic Beanstalk environmnet
- Click your region > Click your eb env > Define simple record > Create records!

#### HTTPS (port 443) 

First we need a certificate. Go to [AWS certificate manager](https://console.aws.amazon.com/acm):

- Request a certificate > Request a public certificate > Add your domain name
- DNS validation > Next > Review (no tags) > Confirm and request
- IMPORTANT! Click the domain arrow and there should be a button `Create record in Route 53`
- Click this button and follow the steps > Confirm

Now go back to eb console. Go to load balancer configuration:

- Add listener on 443 with HTTPS protocol 
- Click apply on bottom right of page

Now go to your [EC2 instance](https://console.aws.amazon.com/ec2/v2) to force https connections:

- Click load balances on bottomish of the left sidebar
- Select the EC2 instance for your eb environment
- Click listeners
- Select port 80
- Edit
- Delete default action 
- Add action > Redirect to... > https port 443
- Update

## Other
 
 - [Uncompromising .gitignore](.gitignore)
 - [env_keys.py](env_keys.py) for handling api keys
 - [discord_notifications.py](discord_notifications.py) for easy notifications 
 - [Python black](https://github.com/psf/black) for formatting

### Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in the unlicense:

> Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.


### Contact 

If you'd like to contact me, please connect with me on [LinkedIn](https://www.linkedin.com/in/daniel-blessing-122806137/). Thank you!