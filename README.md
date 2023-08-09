# Реферальная система.

Сервис разработан на django rest framework

## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone https://github.com/Timur-Razzakov/Hammer_Systems_test.git
````

2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение:

````
source\venv\bin\activate
````

5. В файле .evn заполнить необходимые данные

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432

SECRET_KEY=
DEBUG=
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 132.226.209.39 0.0.0.0 [::1]

API_URL=http://0.0.0.0:8000/api/
```

6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:

```
python manage.py makemigrations
python manage.py migrate
```

8. Запустить сервер

```
python manage.py runserver 0.0.0.0:8000
```

***

# Установка проекта с помощью docker-compose

1. Склонировать репозиторий с Github

```
git clone https://github.com/Timur-Razzakov/Hammer_Systems_test.git
```

2. Перейти в директорию проекта


3. В файле .evn заполнить необходимые данные

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=db
POSTGRES_PORT=5432

SECRET_KEY=
DEBUG=
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1  0.0.0.0 [::1]

API_URL=http://0.0.0.0:8000/api/
```

4. Запустить контейнеры

``` 
sudo docker-compose up -d
 ```

5. Остановка работы контейнеров

```
sudo docker-compose stop
```

***
```http://127.0.0.1:8000/api/registration/``` - выводит форму для номера

```http://127.0.0.1:8000/api/verify_code/``` - авторизация пользователей, путём получения кода

```http://0.0.0.0:8000/``` - Выводит форму, где нужно ввести реферальный invite_code

```http://0.0.0.0:8000/logout/``` - Выход

```http://0.0.0.0:8000/api/referral/``` - Выводит словарь, с номером и количеством подписчиков, а так же чьим
рефералом вы являетесь

```http://0.0.0.0:8000/docs/``` - документация проекта

***

# Есть User-интерфейс
