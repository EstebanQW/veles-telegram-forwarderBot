import asyncio
import re

from telethon import TelegramClient, events

# создание API_ID и API_HASH - https://core.telegram.org/api/obtaining_api_id
API_ID = "api_id"  # взять с https://my.telegram.org/apps
API_HASH = "api_hash"  # взять с https://my.telegram.org/apps
PHONE_NUMBER = "+1234567890"  # ваш номер телефона в формате +1234567890
CHANNEL_NAME = "channel_name"  # имя вашего канала без @
SESSION_NAME = "session_name"  # название сессии, можно указать любое
BOT_NAME = "@VelesFinanceBot"  # имя бота Veles с @

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


def extract_coin_info(message):
    coin_match = re.search(r"(\w+)\s*\|\s*(\w+)", message)

    if not coin_match:
        return None, None, None

    coin_name = coin_match.group(1)  # Название монеты
    position = coin_match.group(2)  # Позиция "LONG" или "SHORT"

    average_price_match = re.search(r"Средняя цена:\s*([\d,]+)", message)
    average_price = average_price_match.group(1) if average_price_match else None

    return coin_name, position, average_price


@client.on(events.NewMessage(chats=BOT_NAME))
async def handler(event):
    original_message = event.message.message
    coin_name, position, average_price = extract_coin_info(original_message)

    if not coin_name:
        print("--------\nSKIP\n", original_message, "\n--------")
        return

    if (
        "1 из" in original_message
        and "Сделка завершена по тейк-профиту." not in original_message
        and position
        and average_price
    ):
        modified_message = (
            f"Захожу в {position} по {coin_name} \n"
            f"Зашел по цене: {average_price}\n\n"
            f"Binance: https://www.binance.com/ru/futures/{coin_name}USDT\n"
            f"OKX: https://www.okx.com/ru/trade-swap/{coin_name}-usdt-swap"
        )
        await client.send_message(CHANNEL_NAME, modified_message)

    elif "Сделка завершена по тейк-профиту." in original_message:
        modified_message = f"Закрыл сделку по {coin_name}"
        await client.send_message(CHANNEL_NAME, modified_message)

    elif "Средняя цена:" in original_message and average_price:
        modified_message = (
            f"Усредняюсь по {coin_name} \nСредняя цена входа: {average_price}"
        )
        await client.send_message(CHANNEL_NAME, modified_message)

    else:
        print(
            "--------\nSKIP: Неизвестный формат сообщения\n",
            original_message,
            "\n--------",
        )


async def main():
    try:
        await client.start(phone=PHONE_NUMBER)
        print("Бот запущен и готов к работе.")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        await client.disconnect()
        print("Бот завершил работу.")


if __name__ == "__main__":
    asyncio.run(main())
