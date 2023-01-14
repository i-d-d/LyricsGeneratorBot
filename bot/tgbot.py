import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import publisher

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello_message(message: types.Message):
    await message.reply("Hi, I am bot that can generate 80-90s rock music lyrics. Try /menu for more info.")


@dp.message_handler(commands=['menu'])
async def menu_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("About dataset")
    button2 = types.KeyboardButton("Generate lyrics")
    markup.add(button1, button2)
    await bot.send_message(message.chat.id, "You can generate new lyrics or get more knowledge "
                                            "about dataset I was trained on", reply_markup=markup)


@dp.message_handler(commands=['generate'])
async def generator(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(message.chat.id, "Generating lyrics (it usually takes around 20 seconds)",
                           reply_markup=markup)
    publisher.publish(str(message.chat.id))


@dp.message_handler(content_types=['text'])
async def answer(message):
    if message.text == "Hello":
        await bot.send_message(message.chat.id, "Hi, my fellow metalhead. Wanna generate some good lyrics today?")
    elif message.text == "Generate lyrics":
        await bot.send_message(message.chat.id, "The generation starts via /generate command")
    elif message.text == "About dataset":
        await bot.send_message(message.chat.id, "I was trained on such good bands like Metallica, Pantera,"
                                                "Nirvana, Iron Maiden, Seether etc. Check them out!")
    else:
        await bot.send_message(message.chat.id, "I can't understand you, I am headbanging too much")


if __name__ == "__main__":
    executor.start_polling(dp)
