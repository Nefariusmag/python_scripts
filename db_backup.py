#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gzip, os, time, datetime, sys,
from sh import pg_dump
# import telebot
# from telebot import types, apihelper

db_host = 'localhost'
db_user = 'postgres'
db_pass = ""
disk_need_size = 20
finish_day = 7
path = "/mnt/backup"
system_mount_path = '/mnt/backup'
list_db = ['one', 'two']

current_time = time.time()

# chat_id = ""
# bot = telebot.TeleBot('')
# apihelper.proxy = {'https':'socks5://'}

for i in os.listdir(path):
    if '.gz' in i:
        creation_time = os.path.getctime(i)
        if (current_time - creation_time) // (24 * 3600) > finish_day:
            os.remove(i)

file_system_mount = os.statvfs(system_mount_path)
disk_size = int((file_system_mount.f_bsize * file_system_mount.f_bavail) / 10**9)

if disk_size <= disk_need_size:
    # message = "На " + db_host + " нехватает места для создания дампа"
    # bot.send_message(chat_id, message)
    sys.exit()


try:
    for i in list_db:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        with gzip.open('backup_' + db_host + '_' + i + '_' + current_datetime + '.gz', 'wb') as f:
            pg_dump('-h', db_host, '-U', db_user, i, _out=f)
except Exception as e:
    # message = "На " + db_host + " не удалось создать дамп"
    # bot.send_message(chat_id, message)
    sys.exit()
