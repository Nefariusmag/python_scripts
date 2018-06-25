#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot, argparse, random
from telebot import types, apihelper

# API key телеграмовского бота
bot = telebot.TeleBot('-')

# список прокси серверов
list_proxy = ('antimalware:eL2S5JbU@148.251.151.141:1080', '121860960:FO8qJhxT@phobos.public.opennetwork.cc:1090', '121860960:FO8qJhxT@deimos.public.opennetwork.cc:1090', 'userid00wa:ZY1iTEi4@185.36.191.39:6398')
# import urllib.request
# url = 'http://proxy_list.py'
# urllib.request.urlretrieve(url, './proxy_list.py')
# import proxy_list
# list_proxy = proxy_list.list_proxy

parser = argparse.ArgumentParser()
parser.add_argument('-m', dest='message', default='Я родился!', help="Сообщение, которое будет отправлено в чат")
parser.add_argument('-id', dest='chat_id', default='-', help="id телеграма чата куда будет отправлено сообщение")
args = parser.parse_args()

all_ok = None
while all_ok != 'ok':
    try:
        apihelper.proxy = {'https':'socks5://' + random.choice(list_proxy)}
        bot.send_message(args.chat_id, args.message)
        all_ok = "ok"
    except Exception as e:
        pass

# запускается с параметрами:
# ./telegram_message.py -id 'id chat or user' -m "some TEXT"
