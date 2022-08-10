
- Создаем виртуальное окружение python -m venv env
- Активируем виртуальное окружение env\Scripts\activate
- Устанавливаем зависимости pip install -r requirements.txt
- Запускаем проект -  python manage.py runserver


SuperUser - email: shpeeck@gmail.com, name: admin, pass: admin123
user - jenya_vas@mail.ru zx78op00
auth_token - 90482ac416a068ebc3feea0a37a9c3961b193a9c

-------------------------------------------
Endpoints
- http://127.0.0.1:8000/api/all-news/ - все новости с пагинацией
- http://127.0.0.1:8000/api/all-news/?category=%D1%81%D0%BF%D0%BE%D1%80%D1%82 - фильтр по категории
- http://127.0.0.1:8000/api/all-news/?search=foo - поиск по названию
- http://127.0.0.1:8000/api/post/2 - получение одного поста (2 - id поста)
- http://127.0.0.1:8000/auth/token/login/ - логин и получение токена
- ###http://127.0.0.1:8000/auth/users/me/ - информация о юзере
- http://127.0.0.1:8000/api/get/profile/ - информация о юзере
- http://127.0.0.1:8000/api/put/profile/ - изменение данных о юзере
- http://127.0.0.1:8000/api/patch/profile/ - изменение данных о юзере
- http://127.0.0.1:8000/api/like/2/ - лайк, дизлайк (2 - id поста)
- http://127.0.0.1:8000/api/post_comment/2/ - добавить коментарий (2 - id поста)
- http://127.0.0.1:8000/api/categories/ - список всех тематик и поиск
- http://127.0.0.1:8000/api/categories/?search=%D0%BF%D0%BE - поиск по тематикам
- http://127.0.0.1:8000/api/top-news/ - топ новостей (более 10 лайков и коментариев)



