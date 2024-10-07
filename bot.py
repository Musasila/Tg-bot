import logging


from aiogram import Bot, Dispatcher, Executor, types


API_TOKEN = '6731743916:AAEkVaf69ge1_VfK-rNm91sAX9-dyjTls7E'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands={'start','help'})
async def send_welcome(message: types.Message);


await message.reply("Hi!/I`m Echobot/Powered by telegram.")

@dp.message_handler()
async def echo(message: types.Message);


await message.answer(message.text)

if __name__ == '__main__';
executor.start_polling(dp, skip_updates=True)
