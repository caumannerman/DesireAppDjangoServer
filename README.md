# DesireAppDjangoServer

가상환경 설치 등은 macOS 기준으로 작성합니다.

## Virtual Environment Setup

```sh
$ pip3 install virtualenv
$ virtualenv venv # Create virutal environment
$ pip3 install -r requirements.txt # Install required packages
```

## Activate virutal environment

```sh
$ source ./venv/bin/activate
(venv) $
```

## Run server

```sh
(venv) $ python3 manage.py runserver
```
