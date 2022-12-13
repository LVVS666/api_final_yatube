#Проект api_final_Yatube
##Описание проекта: Благодаря этому проекту зарегистрированные пользователи могут:

 *Создавать новые посты, комментировать посты других авторов
 *Получать информацию о постах, группах постов и комментариев к постам, оставленные пользвателями
 *Вносить изменения и удалять свои посты и комментарии
 *Подписываться на авторов других постов</li>
 
##Технологии: 
*Python 3.7.9
*Django 2.2.16

##Запуск проекта в dev-режиме

*Установите и активируйте виртуальное окружение python3 -m venv venv source venv/bin/activate
*Установите зависимости из файла requirements.txt
*pip3 install -r requirements.txt
*Примените миграции - python3 manage.py makemigrations python manage.py migrate
*Запустите сервер: python3 manage.py runserver</li>
  
##Примеры запросов:
*Пример запроса GET.posts:http://127.0.0.1:8000/api/v1/posts/
*Припер ответа GET.posts: {"id": 0,"author": "string","text": "string","pub_date": "2019-08-24T14:15:22Z","image": "string","group": 0}

*Пример запроса POST.posts:http://127.0.0.1:8000/api/v1/posts/
*Приvер ответа POST.posts: {{"text": "string","image": "string","group": 0}

*Пример запроса GET.comments:http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
*Припер ответа GET.comments: [{"id": 0,"author": "string","text": "string","created": "2019-08-24T14:15:22Z","post": 0}]

*Пример запроса GET.follow:http://127.0.0.1:8000/api/v1/follow/
*Припер ответа GET.follow: [{"user": "string","following": "string"}]

    
###Более подробная документация доступна по ссылке: http://127.0.0.1:8000/redoc/

Использовать проект можно при помощи Postman Проект доступен только для зарегистированных пользователей Создать пользователя в БД можно командой createsuperuser

*Автор проекта: Логинов Василий*
