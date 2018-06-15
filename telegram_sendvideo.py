#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot, argparse, random
from telebot import types, apihelper

# API key телеграмовского бота
bot = telebot.TeleBot('-')

# список прокси серверов
list_proxy = ('antimalware:eL2S5JbU@148.251.151.141:1080', )

parser = argparse.ArgumentParser()
parser.add_argument('-w', dest='state', default='false', help="Успех или провал отображаем")
parser.add_argument('-id', dest='chat_id', default='-', help="id телеграма чата куда будет отправлено сообщение")
args = parser.parse_args()

if args.state == 'true':
    sti = open("true.webp", 'rb')
elif args.state == 'false':
    sti = open("false.webp", 'rb')

all_ok = None
while all_ok != 'ok':
    try:
        apihelper.proxy = {'https':'socks5://' + random.choice(list_proxy)}
        bot.send_sticker(args.chat_id, sti)
        all_ok = "ok"
    except Exception as e:
        pass

# запускается с параметрами:
# ./telegram_sendvideo.py -id 'id chat or user' -w "true\false"
