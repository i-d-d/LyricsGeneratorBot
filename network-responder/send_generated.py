import config
from aiogram import Bot
import asyncio


async def send_message(chat_id, message):
    operator = Bot(token=config.BOT_API_TOKEN)
    await operator.send_message(chat_id, message)
    await operator.close()


def respond(chat_id, message):
    asyncio.run(send_message(chat_id, message))

