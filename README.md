# Для чего этот скрипт

Этот скрипт предназначен для копирования сообщений из Telegram-бота Veles и их отправки в другой канал. Скрипт использует библиотеку Telethon для работы с Telegram API.

## Настройка скрипта

Получите `API_ID` и `API_HASH`, инструкция - https://core.telegram.org/api/obtaining_api_id. <br>

Откройте файл скрипта. <br>
Замените значения переменных на свои: <br>
`API_ID` = "api_id" - взять с https://my.telegram.org/apps <br>
`API_HASH` = "api_hash" - взять с https://my.telegram.org/apps <br>
`PHONE_NUMBER` = "+1234567890" - ваш номер телефона в формате +1234567890 <br>
`CHANNEL_NAME` = "channel_name" - имя вашего канала (куда будут пересылаться сообщения) без @ <br>
`SESSION_NAME` = "session_name" - название сессии, можно указать любое, либо не менять <br>
`BOT_NAME` = "@VelesFinanceBot" -имя бота Veles с @ <br>

## Установка названия бота Veles
Необходимо в названии бота указать монету и позицию через "|" <br>
Пример:<br>
`OP | LONG` <br>
`BTC | SHORT` <br>
`ETH | LONG` <br>

## Запуск скрипта

1. Установите необходимые зависимости: <br>

```
pip install telethon
```

2. Запустите скрипт: <br>

```
python main.py
```

## Авторизация

Введите код подтверждения, который придет в Telegram: <br>

```
Please enter the code you received:
```
![image](https://github.com/user-attachments/assets/8777d0b2-2083-4353-a543-82c8b79c9278) <br>


Если на аккаунте стоит облачный пароль, то его также нужно будет ввести, после сообщения и нажать Enter: <br>

```
Please enter your password:
```

## Проверка работы

Скрипт начнет обрабатывать сообщения от указанного бота (`BOT_NAME`). <br>
Обработанные сообщения будут пересылаться в указанный канал (`CHANNEL_NAME`). <br>
Пропущенные или неизвестные сообщения будут выводиться в консоль. <br>

Пример работы скрипта: <br>


|Событие|Сообщение в боте Veles|Сообщение в вашем канале|
|:---|:---|:---|
|**Открытие позиции**|![image](https://github.com/user-attachments/assets/cfb51f75-4bbf-4eb2-bf15-422babf0410a)|![image](https://github.com/user-attachments/assets/c481c845-c089-45d7-afb7-087a57cf8589)|
|**Усреднение**|![image](https://github.com/user-attachments/assets/5c3c066a-d6e6-4375-ab77-88f94fd1bbde)|![image](https://github.com/user-attachments/assets/890e66fc-7bab-40d2-a850-1f42c4ef3a7e)|
|**Тейк профит**|![image](https://github.com/user-attachments/assets/e4433dcb-5c0c-49b1-9f79-6bd0797a5c47)|![image](https://github.com/user-attachments/assets/4d035b34-6e24-494e-a2c7-745e8d94886a)|

Если сообщение не соответствует ожидаемому формату, оно будет пропущено, и в консоли появится запись: <br>

```
--------
SKIP: Неизвестный формат сообщения
[Текст сообщения]
--------
```
