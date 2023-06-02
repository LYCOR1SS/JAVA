import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6003040010:AAFF1Tp5p7IVWo6OEjSBoxMjvnrYNh9XSkY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



import requests

# Получение статьи по названию
def get_wiki_article(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "exintro": "",
        "explaintext": "",
        "redirects": "",
        "formatversion": "2"
    }
    response = requests.get(url, params=params).json()
    return response['query']['pages'][0]['extract'] if response['query']['pages'][0]['extract'] else None

# Пример использования
article = get_wiki_article("Python Programming Language")
print(article)


#bot = telebot.TeleBot("6220529358:AAFrf1XAUcNJR4vI-si4BKgzUXxBZK5dFXI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот Википедии на Python! Какую статью вы бы хотели найти?")

@bot.message_handler(func=lambda message: True)
def search_wiki_article(message):
    article = get_wiki_article(message.text)
    if article:
        bot.reply_to(message, article)
    else:
        bot.reply_to(message, "Я не смог найти такую статью.")
    
bot.polling()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)