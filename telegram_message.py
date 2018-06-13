#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen
import argparse

api_key = "---" # API key телеграмовского бота

parser = argparse.ArgumentParser()
parser.add_argument('-w', dest='work', default='false',  help="Проверка на разрешение на отправку сообщения")
parser.add_argument('-m', dest='message', default='Я родился!', help="Сообщение, которое будет отправлено в чат")
parser.add_argument('-t', dest='issue_id', type=int,  default=0, help="Номер задачи для перевода в тестирование, 0 - без задачи")
parser.add_argument('-id', dest='chat_id', default='-', help="id телеграма чата куда будет отправлено сообщение")

args = parser.parse_args()

issue_text = "Задача http://redmine-energo.dkp.lanit.ru/issues/{}".format(args.issue_id)

if args.issue_id > 0:
    args.message = args.message + "\n\n" + issue_text
    args.chat_id = "--"

turl = 'https://api.telegram.org/bot'
tfull = '{0}{1}/sendMessage'.format(turl, api_key)

tparams = urlencode({'chat_id': args.chat_id, 'text': args.message}).encode('utf-8')

if args.work == "true":
    urlopen(tfull, tparams)

# запускается с параметрами:
# ./telegram_message.py -w ${telegram_message} -id - -t ${issue_id} -m "some TEXT"
