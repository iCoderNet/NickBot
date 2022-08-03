import logging

from aiogram import Bot, Dispatcher, executor, types
import random
from time import sleep
from func import *


API_TOKEN = '5555066325:AAFHtggq77cnnwwNYyEZ2Byl-WQDSqfkfNM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("• Aѕѕαℓσмυ Aℓαукυм\n• Bσтιмιzgα Xυѕн кєℓιвѕιz\nCнιяσуℓι Nιкℓαя уαѕαѕн υ¢нυη ιѕмιηgιzηι уυвσяιηg уσкι ραѕт∂αgι тυgмαηι вσѕιв ιηℓιηє яєנιм∂αη ƒσу∂αηαℓιηg 👇🏻",  reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⚙️ Foydalanish", switch_inline_query="ism")))


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'You'
    rs = []
    for i in make_nick(text):
        id = random.randint(1,2242252682114)
        i_van = types.InlineQueryResultArticle(
            id=id,
            thumb_url="https://i.imgur.com/KsIumPH.jpg",
            title=i,
            description=i,
            input_message_content=types.InputTextMessageContent(i),
        )
        rs.append(i_van)
    await inline_query.answer(results=rs, cache_time=1)


@dp.message_handler()
async def nick(message: types.Message):
    for i in make_nick(message.text):
        await message.answer(i)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)