# Notification app
Notification app это веб приложение которое позовляет создавать и изменять уведомления и отправлять их по вебсокет.

## Как установить

Скопируете проект: ` git clone https://github.com/Grindmix/notification-app.git `

Запустите контейнер: `docker compose up --build `

Вебсокет адрес: `ws://host:port/ws/notifications/`

Для тестирования можно воспользоваться <a href="https://github.com/Grindmix/wscli"> этим </a> вебсокет клиентом

## Эндпоинты

- Создать уведомление: `POST api/notifications/`

Тело запроса: 
```json 
{
    "title" : "Название",
    "type": "SUCCESS/WARNING/FAIL",
    "content": "Описание"
}
```

- Получить список всех уведомлений: `GET api/notifications/`

- Получить уведомление по id: `GET api/notifications/{id}/`

- Обновить уведомление по id: `PUT api/notifications/{id}/`

- Удалить уведомление по id: `DELETE api/notifications/{id}/`

- Отправить уведомление по вебсокет: `POST api/notifications/send/{id}/`

Отправить в определнное время (необязательно):
```json
{
    "sendAt": "dd/mm/yy hh:mm:ss"
}
```

Часовой пояс определяется в `settings.py` переменной TIME_ZONE

