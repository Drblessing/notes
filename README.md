# Utils

My mega awesome repo of all development and related tips and tricks I've learned along the way, such as:

- Current IDE: VSCode
- Current Laptop: MacBook Pro (16-inch, 2021)
- Laptop Setup: Apps, Virus Protection, Workflows, Keyboard Shortcuts, etc.
- IDE Setup: VSCode Favorite Extensions, Default Keyboard Shortcuts, Snippets, Custom Keyboard Shortcuts, etc.
- Full stack Dev Tips: NextJS, Typescript, etc.
- Blockchain Dev Tips: Crypto tips and tricks

This repo is mainly for myself, though if you read it and get some value from it that would make me smile. Furthermore, if you have some useful tips and tricks from your dev journey, please send a PR!

Info Styled as a FAQ

## Cool Stuff

- Deepsource / Deepscan
- Blockchair
- https://scrape.do/

## HTTP Request Tester

https://http.dog/

## Python quickstart

### Install Python

- [Install anaconda](https://www.anaconda.com/products/individual)
- Homebrew
- venv

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

Adding new environments to jupyter

```shell
$ (venv) pip install ipykernel
$ (venv) pip install ipython
$ (venv) python -m ipykernel install --user --name=my-virtualenv-name
```

Deal with jupyter kernel errors

```shell
$ jupyter kernelspec list
$ jupyter kernelspec remove <kernel-name>
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
{% block head %} {{ super() }} {% include "ga.html" %} {% endblock %}
```

Deploy flask directly to [aws elastic beanstalk](https://aws.amazon.com/elasticbeanstalk/), [pythonanywhere](https://www.pythonanywhere.com/), or [more options here](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html).

Or, build a [Docker image](Dockerfile), and deploy to [aws elastic beanstalk](https://aws.amazon.com/elasticbeanstalk/) or [more options here](https://geekflare.com/docker-hosting-platforms/).

### [Elastic Beanstalk Deployment](https://console.aws.amazon.com/elasticbeanstalk)

#### Upload and Deploy

Manually zip your files with no parent directory and upload directly to eb environments in your applications.

For Flask envs, elastic beanstalk launches from `application` flask object in the root directory.

For Docker envs, elastic beanstalk launches from `Dockerfile` and `Dockerrun.aws.json` in the root directory. Implement a WSGI.

#### [EB CLI](https://github.com/aws/aws-elastic-beanstalk-cli-setup)

For big brains, manage eb from the command line.

Build a `deploy.sh` script and requires a `docker-compose.yaml` file.

#### Other Deployment methods

You can also deploy environments from s3 buckets or private/public Docker repositories.

### Elastic Beanstalk Configuration

Environments > Configuration on sidebar

To manage maximum scaling up, edit the max field in capacity. If you set max to 1 you can limit potential max cost.
For cores per instance, check [here](https://aws.amazon.com/ec2/physicalcores/). For gunicorn, roughly # workers = # cores \* 2 + 1

#### Better Domain

For last-minute maximal convenience, purchase a domain from Amazon Route 53 [here](https://console.aws.amazon.com/route53/v2).

`.io` domains are in vogue now.

If you're creating a crypto rugpull, consider a `.finance` domain.

To point your new shiny domain name to your eb environment:

- Go to AWS Route 53 > Hosted Zone > Domain name
- Create Record > Wizard Create > Simple Routing
- Define Simple Record > Value/Route Traffic to > Alias to Elastic Beanstalk environmnet
- Click your region > Click your eb env > Define simple record > Create records

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

### IPFS Node

```bash
wget https://dist.ipfs.io/go-ipfs/v0.7.0/go-ipfs_v0.7.0_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.7.0_linux-amd64.tar.gz
cd go-ipfs
bash install.sh
ipfs --version
ipfs init
ipfs daemon
```

### Eth node

## Other

- [Uncompromising .gitignore](.gitignore)
- [env_keys.py](env_keys.py) for handling api keys
- [discord_notifications.py](discord_notifications.py) for easy notifications
- [Python black](https://github.com/psf/black) for formatting

### Public domain

This project is in the worldwide [public domain](LICENSE). As stated in the unlicense:

> Anyone is free to copy, modify, publish, use, compile, sell, or
> distribute this software, either in source code form or as a compiled
> binary, for any purpose, commercial or non-commercial, and by any
> means.

### Contact

If you'd like to contact me, please connect with me on [Twitter](https://twitter.com/dbless9). Thank you!
