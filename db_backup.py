#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time, datetime, sys, argparse, threading, tarfile, shutil
from sh import pg_dump, pg_restore
# import telebot
# from telebot import types, apihelper
from threading import Thread

db_host = 'localhost'
db_user = 'postgres'
db_pass = ""
disk_need_size = 20
finish_day = 7
cpu = 4
path = "/mnt/backup"
system_mount_path = '/mnt/backup'
list_db = ['one', 'two']

current_time = time.time()

# chat_id = ""
# bot = telebot.TeleBot('')
# apihelper.proxy = {'https':'socks5://'}

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest='state', default='dump', help="Dump or restore")
parser.add_argument('-f', dest='files_dump', help="Файл для восстановления")
parser.add_argument('-d', dest='database', help="База для восстановления")
args = parser.parse_args()

def gziping(folder):
    tar = tarfile.open(folder + ".tar.gz", "w:gz")
    tar.add(folder, arcname=folder)
    tar.close()
    shutil.rmtree(folder)

if args.state == 'dump':
    for i in os.listdir(path):
        if '.gz' in i:
            creation_time = os.path.getctime(i)
            if (current_time - creation_time) // (24 * 3600) > finish_day:
                os.remove(i)
    file_system_mount = os.statvfs(system_mount_path)
    disk_size = int((file_system_mount.f_bsize * file_system_mount.f_bavail) / 1000000000)
    if disk_size <= disk_need_size:
        message = "На " + db_host + " нехватает места для создания дампа"
        bot.send_message(chat_id, message)
        sys.exit()
    try:
        for database in list_db:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
            pg_dump('-h', db_host, '-U', db_user, '-d', database, '--encoding=UTF8', '-j', cpu, '--format=directory', '-f', 'backup_' + db_host + '_' + database + '_' + current_datetime)
            t = Thread(target=gziping, args=('backup_' + db_host + '_' + database + '_' + current_datetime,))
            t.start()
    except Exception as e:
        message = "На " + db_host + " не удалось создать дамп"
        bot.send_message(chat_id, message)

if args.state == 'restore':
    # tar = tarfile.open(args.files_dump)
    # tar.extractall()
    # tar.close()
    pg_restore('-h', db_host, '-U', db_user, '-d', args.database, '-j', cpu, args.files_dump)
