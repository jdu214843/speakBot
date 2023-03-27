import logging


from aiogram import Bot, Dispatcher, executor, types


from oxfortranslate import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '5793605726:AAGn64dmANz8OUA2c2lgIChc4JV00TZdbf0'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Xush Kelibsiz! Kompyuter ilmlari botiga")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):

    await message.reply("Xush Kelibsiz! qanday yordam kerak")


@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi!")
            
            await message.reply("Bunday so'z topilmadi!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
#     nimadir o'zgardi
    
    
    
