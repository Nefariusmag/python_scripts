#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import argparse


bot = telebot.TeleBot("-")

parser = argparse.ArgumentParser()
parser.add_argument('-m', dest='message', default='Я родился!', help="Сообщение, которое будет отправлено в чат")
parser.add_argument('-vm', dest='videomessage', default='false.mp4', help="Видео (true & false), которое будет отправлено в чат")
parser.add_argument('-id', dest='chat_id', default='121860960', help="id телеграма чата куда будет отправлено сообщение")

args = parser.parse_args()


bot.send_message(args.chat_id, args.message)
bot.send_video(args.chat_id, open(args.videomessage, 'rb'))
