# bcschain-display
Приложение для отображения блокчейна BCSChain


## Инструкция по запуску
  - Склонировать репозиторий к себе на компьютер
  - Установить виртуальное окружение и активировать
```shell
python3 -m venv env
source env\bin\activate
```
  - Установить зависимости
```shell
pip3 install -r requirements.txt
```
  - Установить PostgreSQL и ввести свои данные в настройках приложения
```shell
'NAME': '...',
'USER': '...',
'PASSWORD': '...',
```
  - Выполнить миграции
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
  - Создать пользователя для доступа к админке
```shell
python3 manage.py createsuperuser
```
  - Запуск web-приложения
```
python3 manage.py runserver
```

### При первом запуске надо перейти на главную страницу http://127.0.0.1:8000/.  
### Подождать пока загрузяться все блоки блокчейна и заполнится бд. (≈3-4 минуты)
![alt text](https://i.ibb.co/chtFwS0/m9-Gycablq3-Y.jpg)
