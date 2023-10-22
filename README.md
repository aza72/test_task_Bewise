# test_task_Bewise

## Стек технологий

- Язык: Python 3 
- БД: PostgreSQL
- Фрейморк: Django 4
- ORM: Django REST framework
- Среда контейнеров: Docker(docker-compose)
## Инструкция по сборке и запуску
Запуск проекта происходит из директории проекта test_task_Bewise\tesktask_site  в терминале ввести команду "docker-compose up".

## Пример запроса и данные
Адрес админ панели для доступа в БД: "http://localhost:8000/admin"
Логин: "root"
Пароль: "1234"
Пример запроса: "http://127.0.0.1:8000/api/v1/quelist?count=1", где count количество вопросов, которое необходимо получить.
Тест POST запросов производил в программе Postman.
