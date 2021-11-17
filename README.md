# DesireAppDjangoServer

가상환경 설치 등은 macOS 기준으로 작성합니다.

## Virtual Environment Setup

- 가상환경을 생성하고 패키지를 설치합니다.

  ```sh
  $ pip3 install virtualenv
  $ virtualenv venv
  ```

- 가상환경을 활성화합니다.

  ```sh
  $ source ./venv/bin/activate
  (venv) $
  ```

- 가상 환경에 패키지를 설치합니다.

  ```sh
  (venv) $ pip3 install -r requirements.txt
  ```

## Set secrets

- `.env.template` 파일을 복사하여 `.env` 파일을 만들고, `KEY=` 뒤에 값을 알맞게 채워줍니다.

## Setup database

- DB 스키마 등이 변경될 경우 서버 실행 전 다음 명령어를 한번씩 실행합니다.

  ```sh
  (venv) $ python3 manage.py makemigrations # Create migration files
  (venv) $ python3 manage.py migrate # Migrate
  ```

## Create admin user

- Admin 사용자가 필요하면 다음과 같이 실행합니다. (이후 아이디, 이메일, 비밀번호 설정)

  ```sh
  (venv) $ python manage.py createsuperuser
  ```

## Run server

- 개발용으로 runserver를 사용합니다.

  ```sh
  (venv) $ python3 manage.py runserver
  ```

## Debugging

- Django debug shell을 이용합니다.

  ```sh
  (venv) $ python3 manage.py shell
  ```
