# [AWS EC2](https://console.aws.amazon.com/ec2)

## Start

Free t2.micro

Create new ssh key and put it in your .ssh folder

sudo yum install git

## Connecting to jupyter notebook
```bash
$ ssh -i ~/.ssh/my-private-key.pem user-name@remote-hostname
$ jupyter notebook password
$ nohup jupyter notebook --no-browser --port=8888
$ ssh -i my-private-key.pem -N -f -L localhost:8888:localhost:8888 user-name@remote-hostname
```

## Background processes

For temporal interval processes use crontab

For everything else use tmux:

```bash
$ sudo yum install tmux
$ tmux
$ tmux detach
$ tmux attach
```

## Anaconda

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ bash Anaconda3-2021.05-Linux-x86_64.sh
```




