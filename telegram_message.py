#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot, argparse, random
from telebot import types, apihelper

# API key телеграмовского бота
bot = telebot.TeleBot('-')

# список прокси серверов
list_proxy = ('193.112.141.244:1080', '131.72.22.128:39880', '192.169.138.2:7959', '65.182.107.208:8975', '109.108.89.17:39880')

apihelper.proxy = {'https':'socks5://' + random.choice(list_proxy)}

parser = argparse.ArgumentParser()
parser.add_argument('-w', dest='work', default='false',  help="Проверка на разрешение на отправку сообщения")
parser.add_argument('-m', dest='message', default='Я родился!', help="Сообщение, которое будет отправлено в чат")
parser.add_argument('-t', dest='issue_id', type=int,  default=0, help="Номер задачи для перевода в тестирование, 0 - без задачи")
parser.add_argument('-id', dest='chat_id', default='-', help="id телеграма чата куда будет отправлено сообщение")
args = parser.parse_args()

if args.issue_id > 0:
    issue_text = "Задача http://redmine-energo.dkp.lanit.ru/issues/{}".format(args.issue_id)
    args.message = args.message + "\n\n" + issue_text
    args.chat_id = "-"

if args.work == "true":
    try:
        bot.send_message(args.chat_id, args.message)
    except Exception as e:
        apihelper.proxy = {'https':'socks5://' + random.choice(list_proxy)}
        bot.send_message(args.chat_id, args.message)

# запускается с параметрами:
# ./telegram_message.py -w ${telegram_message} -id -217174145 -t ${issue_id} -m "some TEXT"
