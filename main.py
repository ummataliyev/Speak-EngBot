import logging

from oxfordlookup import getDefinitions

from googletrans import Translator

from aiogram import Bot, Dispatcher, executor, types

translator  = Translator()

API_TOKEN = '5757532837:AAGQxeRmnnh6GgZiJwkDbGg0tH9o5F31mQY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Assalamu alaykum!\nPlease enter the word.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `help` command
    """
    await message.reply("I will show you the information about the word you are looking for and how to pronounce it!")


@dp.message_handler()
async def trans(message: types.Message):
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
            await message.reply("No such word found!\nBunday so'z topilmadi!\n🫠🫠🫠")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
