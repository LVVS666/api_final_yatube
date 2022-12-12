<h1>Проект api_final_Yatube</h1>
Описание проекта: Благодаря этому проекту зарегистрированные пользователи могут:
<ul>
  <li>создавать новые посты, комментировать посты других авторов</li>
<li>получать информацию о постах, группах постов и комментариев к постам, оставленные пользвателями</li>
  <li>вносить изменения и удалять свои посты и комментарии</li>
  <li>Подписываться на авторов других постов</li>
</ul>
 
<b>Технологии: Python 3.7.9 Django 2.2.16</b>

  <h2>Запуск проекта в dev-режиме</h2>
<ul>
<li>Установите и активируйте виртуальное окружение python3 -m venv venv source venv/bin/activate</li>
<li>Установите зависимости из файла requirements.txt</li>
<li>pip3 install -r requirements.txt</li>
<li>Примените миграции - python3 manage.py makemigrations python manage.py migrate</li>
<li>Запустите сервер: python3 manage.py runserver</li>
  
<h2>Примеры запросов:</h2>
<p>Пример запроса GET.posts:http://127.0.0.1:8000/api/v1/posts/</p>
<p> Припер ответа GET.posts: {"id": 0,"author": "string","text": "string","pub_date": "2019-08-24T14:15:22Z","image": "string","group": 0}</p>
<p>Пример запроса POST.posts:http://127.0.0.1:8000/api/v1/posts/</p>
<p> Припер ответа POST.posts: {{"text": "string","image": "string","group": 0}</p>
<p>Пример запроса GET.comments:http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/</p>
<p> Припер ответа GET.comments: [{"id": 0,"author": "string","text": "string","created": "2019-08-24T14:15:22Z","post": 0}]
<p>Пример запроса GET.follow:http://127.0.0.1:8000/api/v1/follow/</p>
<p> Припер ответа GET.follow: [{"user": "string","following": "string"}]

    
<p>Более подробная документация доступна по ссылке: http://127.0.0.1:8000/redoc/

Использовать проект можно при помощи Postman Проект доступен только для зарегистированных пользователей Создать пользователя в БД можно командой createsuperuser
