## ToDoCoreForItPower (тестовое задание на DRF)

Это Rest Api сервер для сайта списка дел реализованный через DRF c авто-документацией Swagger. <br>
-Реализована API CRUD модель для задач(GET, POST, PUT, DELETE). <br>
-Реализована API CRUD  модель для категорий задач(GET, POST, PUT, DELETE). <br>
-Реализована API CRUD модель для работы с пользователями + смена пароля, имени и т.д.(GET, POST, PUT, DELETE). <br>
-Средствами DRF реализована пагинация ( указание количества отображаемых элементов в settings). <br>
-Реализована автоматическая документация API методов Swagger. <br>

Установка: 

1. Склонируйте репозиторий:

```
git clone git@github.com:konmin123/ToDoForItPower.git
```

2. Создайте и активируйте вирутальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Установите зависимости:

```
pip install -r requirements.txt
```  

4. Создайте текстовый файл .env.txt аналогично шаблону template.env.txt

5. Проведите миграции:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

6. Создайте суперпользователя:

```
python manage.py createsuperuser
```

7. Запустите тестовый сервер:

```
python manage.py runserver
```
