# Для чего этот скрипт

Этот скрипт предназначен для копирования сообщений из Telegram-бота Veles и их отправки в другой канал. Скрипт использует библиотеку Telethon для работы с Telegram API.

## Настройка скрипта

Получите `API_ID` и `API_HASH`, инструкция - https://core.telegram.org/api/obtaining_api_id.

Откройте файл скрипта.
Замените значения переменных на свои:
`API_ID` = "api_id" - взять с https://my.telegram.org/apps
`API_HASH` = "api_hash" - взять с https://my.telegram.org/apps
`PHONE_NUMBER` = "+1234567890" - ваш номер телефона в формате +1234567890
`CHANNEL_NAME` = "channel_name" - имя вашего канала (куда будут пересылаться сообщения) без @
`SESSION_NAME` = "session_name" - название сессии, можно указать любое, либо не менять
`BOT_NAME` = "@VelesFinanceBot" -имя бота Veles с @

## Запуск скрипта

1. Установите необходимые зависимости:

```
pip install telethon
```

2. Запустите скрипт:

```
python main.py
```

## Авторизация

Введите код подтверждения, который придет в Telegram:

```
Please enter the code you received:
```

Если на аккаунте стоит облачный пароль, то его также нужно будет ввести, после сообщения и нажать Enter:

```
Please enter your password:
```

## Проверка работы

Скрипт начнет обрабатывать сообщения от указанного бота (`BOT_NAME`).
Обработанные сообщения будут пересылаться в указанный канал (`CHANNEL_NAME`).
Пропущенные или неизвестные сообщения будут выводиться в консоль.

Пример работы скрипта:

Если сообщение не соответствует ожидаемому формату, оно будет пропущено, и в консоли появится запись:

```
--------
SKIP: Неизвестный формат сообщения
[Текст сообщения]
--------
```
