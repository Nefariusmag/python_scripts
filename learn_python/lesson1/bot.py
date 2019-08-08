# Импортируем нужные компоненты
import logging
import ephem
import datetime
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.getenv('TOKEN', '')

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def planet_name(bot, update):
    text = update.message.text.split(' ')[1]
    print(text)
    todat_date = datetime.date.today()
    print(todat_date)
    # try:
    #     exec(f"planet_name = ephem.constellation(ephem.{text}({todat_date}))", globals())
    #     update.message.reply_text(f"{text} находится в созвездии {planet_name[1]}")
    # except AttributeError:
    #     update.message.reply_text(f"Прости, но у нас нету {text} в базе")
    # print(planet_name[1])
    # or
    try:
        planet = getattr(ephem, text)
        planet_with_date = planet(todat_date)
        constellation_planet = ephem.constellation(planet_with_date)
        update.message.reply_text(constellation_planet[1])
    except AttributeError:
        update.message.reply_text(f"Прости, но у нас нету {text} в базе")


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(token, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(update)
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


# Вызываем функцию - эта строчка собственно запускает бота
main()
