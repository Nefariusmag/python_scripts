#!/bin/python
# -*- coding: utf-8 -*-
version = str("0.5") # версия скрипта автоматизации
# Ерохин Д.А.
# i9164871362@gmail.com
### Переменные
# Импорт модулей
import datetime
import os
import shutil
import subprocess
# Время
dt = datetime.datetime.now()
xdate = dt.strftime('%Y-%m-%d_%H:%M')
# Папки
WORK_DIR = str("/opt/ruby_projects")
# Файл сборки, что берем с ftp
rvec = str("rvec_.zip")
# ftp
serverftp1 = str("10.160.20.13")
ftplogin1 = str("-")
ftppassword1 = str("-")
ftpdir1 = str("Software")
# IP-адреса
# Основной комплекс
orcl101 = str("orcl-301-okt")
orcl102 = str("orcl-302-okt")
main101 = str("main-301-okt")
main102 = str("main-302-okt")
drv101 = str("drv-301-okt")
drv102 = str("drv-302-okt")
line101 = str("line-301-okt")
line102 = str("line-302-okt")
line103 = str("line-303-okt")
line104 = str("line-304-okt")
line105 = str("line-305-okt")
line106 = str("line-306-okt")
web101 = str("web-301-okt")
web102 = str("web-302-okt")
# Тренажерный комплекс
orcl201 = str("orcl-301-okt")
orcl202 = str("orcl-302-okt")
main201 = str("main-301-okt")
main202 = str("main-302-okt")
drv201 = str("drv-301-okt")
drv202 = str("drv-302-okt")
line201 = str("line-301-okt")
line202 = str("line-302-okt")
line203 = str("line-303-okt")
line204 = str("line-304-okt")
line205 = str("line-305-okt")
line206 = str("line-306-okt")
web201 = str("web-301-okt")
web202 = str("web-302-okt")
### Функции и массивы
# функци ошибки
def error():
    print ("\nОшибка. Попробуйте еще раз")
# функции выбора для основного комплекса
def vibor_ip():
    global ip_all
    ip_all = str("")
    options = {
    0 : orcl101,
    1 : orcl102,
    2 : main101,
    3 : main102,
    4 : drv101,
    5 : drv102,
    6 : line101,
    7 : line102,
    8 : line103,
    9 : line104,
    10 : line105,
    11 : line106,
    12 : web101,
    13 : web102
    }
    print options
    opt = input("\nВыберите с чем будем работать, через запятую начиная с нуля:\n")
    for lll in opt:
        kkk = options[lll]
        ip_all = ip_all + " " + kkk
    print ("Выбранные сервера: " + ip_all + "\n")
# функции выбора для тренажерного комплекса
def vibor_ip_tren():
    global ip_all
    ip_all = str("")
    options = {
    0 : orcl201,
    1 : orcl202,
    2 : main201,
    3 : main202,
    4 : drv201,
    5 : drv202,
    6 : line201,
    7 : line202,
    8 : line203,
    9 : line204,
    10 : line205,
    11 : line206,
    12 : web201,
    13 : web202
    }
    print options
    opt = input("\nВыберите с чем будем работать, через запятую начиная с нуля:\n")
    for lll in opt:
        kkk = options[lll]
        ip_all = ip_all + " " + kkk
    print ("Выбранные сервера: " + ip_all + "\n")
# функция запуска Вектора start_vektor <ip> <ip> <ip> <ip>
def start_vektor():
    qw = None
    print ip_all
    print ("Для запуска Вектора введите пароль для rvec-adm.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l rvec-adm -i -t 100 \"/etc/init.d/rvec-daemon.sh start; \cp /opt/rvec_cron/check-rvec_backup.sh /opt/rvec_cron/check-rvec.sh\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"EXIT_CODE : 1\"")
            if test != 256:
                print ("\nОшибка при запуске Вектора.")
            test = os.system("cat /opt/pssh.txt | grep \"No space\"")
            if test != 256:
                print ("\nЗакончилось свободное место.")
            qw = raw_input("\nХотите еще раз запустить Вектор? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для запуска Вектора введите пароль для rvec-adm.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Вектор запускается на серверах" + ip_all)
                    qw = str("N")
    else:
        print ("Вектор запускается на серверах" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция остановки Вектора stop_vektor <ip> <ip> <ip>
def stop_vektor():
    qw = None
    print ip_all
    print ("Для остановки Вектора введите пароль для rvec-adm.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l rvec-adm -i -t 100 \"echo > /opt/rvec_cron/check-rvec.sh; /etc/init.d/rvec-daemon.sh stop\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"EXIT_CODE : 1\"")
            if test != 256:
                print ("\nОшибка при остановке Вектора.")
            test = os.system("cat /opt/pssh.txt | grep \"No space\"")
            if test != 256:
                print ("\nЗакончилось свободное место.")
            test = os.system("cat /opt/pssh.txt | grep \"No pid file, not stopping\"")
            if test != 256:
                print ("\nУже остановлен.")
            qw = raw_input("\nХотите еще раз запустить Вектор? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для остановки Вектора введите пароль для rvec-adm.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Вектор остановлен на серверах" + ip_all)
                    qw = str("N")
    else:
        print ("Вектор остановлен на серверах" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция перезапуска <ip> <ip> <ip>
def restart_vektor():
    qw = None
    print ("Для перезапуска Вектора введите пароль для rvec-adm.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l rvec-adm -i -t 100 \"/etc/init.d/rvec-daemon.sh restart\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"EXIT_CODE : 1\"")
            if test != 256:
                print ("\nОшибка при перезапуске Вектора.")
            test = os.system("cat /opt/pssh.txt | grep \"No space\"")
            if test != 256:
                print ("\nЗакончилось свободное место.")
            qw = raw_input("\nХотите еще раз перезапустить Вектор? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для перезапуска Вектора введите пароль для rvec-adm.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Вектор перезапущен на серверах" + ip_all)
                    qw = str("N")
    else:
        print ("Вектор перезапущен на серверах" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция обновления obnova <ip> <ip> <ip>
def obnova():
    qw = None
    print ("Для обновления Вектора введите пароль для rvec-adm.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l rvec-adm -i -t 100 \"mv " + WORK_DIR + "/rvec " + WORK_DIR + "/old/rvec_$xdate; unzip -d " + WORK_DIR + "/ " + WORK_DIR + "/rvec.zip; /bin/cp " + WORK_DIR + "/conf/* " + WORK_DIR + "/rvec/conf/; chmod +x -R " + WORK_DIR + "/rvec; chown -R rvec-adm:rvec-adm " + WORK_DIR + "/rvec\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"EXIT_CODE : 1\"")
            if test != 256:
                print ("\nОшибка при запуске Вектора.")
            test = os.system("cat /opt/pssh.txt | grep \"No space\"")
            if test != 256:
                print ("\nЗакончилось свободное место.")
            qw = raw_input("\nХотите еще раз обновить Вектор? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для обновления Вектора введите пароль для rvec-adm.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Вектор обновлен на серверах" + ip_all)
                    qw = str("N")
    else:
        print ("Вектор обновлен на серверах" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция скачивания с ftp download <ip> <ip> <ip>
def download():
    qw = None
    print ("Для загрузки с ftp новой версии Вектора, введите пароль для rvec-adm.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l rvec-adm -i -t 1500 \"wget -t 25 ftp://" + ftplogin1 + ":" + ftppassword1 + "@" + serverftp1 + "/" + ftpdir1 + "/" + rvec + " -O " + WORK_DIR + "/rvec.zip\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"EXIT_CODE : 1\"")
            if test != 256:
                print ("\nОшибка при загрузке Вектора.")
            test = os.system("cat /opt/pssh.txt | grep \"No space\"")
            if test != 256:
                print ("\nЗакончилось свободное место.")
            test = os.system("cat /opt/pssh.txt | grep \"Timed out\"")
            if test != 256:
                print ("\nНе дождались загрузки с ftp. Возможно проблемы с соединением.")
            qw = raw_input("\nХотите еще раз скачать новую сборку Вектора? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для загрузки с ftp новой версии Вектора, введите пароль для rvec-adm.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Cборка загруженна на сервера" + ip_all)
                    qw = str("N")
    else:
        print ("Cборка загруженна на сервера" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция вопроса о ftp
def ftp_ok():
    print "***********************************************"
    print " Для обновления серверов с ftp необходимо скачать обновление"
    print " Обновление скопированно?"
    print " Да - Y"
    print " Нет, но хочу скачать и начать обновление - L"
    print " Нет - N"
    item = raw_input()
# функция для доступа разработчиков dostup <ip> <ip> <ip> <ip>
def dostup():
    qw = None
    print ("Для расшаривания логов введите пароль для root.")
    zap = str("pssh -A -H \"" + ip_all + "\" -l root -i -t 100 \"setfacl -R -m u:user1:rx " + WORK_DIR + "/rvec/conf\" > /opt/pssh.txt")
    os.system(zap)
    test = os.system("cat /opt/pssh.txt | grep FAILURE")
    if test != 256:
        while qw != "N":
            test = os.system("cat /opt/pssh.txt | grep Permission")
            if test != 256:
                print ("\nОшибка. Ввели неверный пароль.")
            test = os.system("cat /opt/pssh.txt | grep \"Нет такого файла или каталога\"")
            if test != 256:
                print ("\nОшибка. Нет такого файла или каталога.")
            test = os.system("cat /opt/pssh.txt | grep \"Недопустимый аргумент near character 3\"")
            if test != 256:
                print ("\nОшибка. Пользователь user1 не создан.")
            qw = raw_input("\nХотите еще раз расшарить логи? (Y)es. (N)o.\n")
            if qw != "N":
                print ("Для расшаривания логов введите пароль для root.")
                os.system(zap)
                test = os.system("cat /opt/pssh.txt | grep FAILURE")
                if test == 256:
                    print ("Логи расшарены на" + ip_all)
                    qw = str("N")
    else:
        print ("Логи расшарены на" + ip_all)
    os.system("rm -rf /opt/pssh.txt")
# функция на выход
def ex():
    print ("Выход.")
    exit()
# функция меню 1
def text1():
    os.system('clear')
    print ("""
    Меню управления. Выберите комплекс:
1) - Основной комплекс.
2) - Тренажерный комплекс.
Q) - Выйти.
""")

# функция меню
def text2():
    os.system('clear')
    print ("""
    Меню обновления:
1) - Остановка серверов.
2) - Запуск серверов.
3) - Перезапуск серверов.
4) - Обновление ПО Вектор-M.
0) - Перенос с ftp актуального дистрибутива ПО Вектор-М.
Q) - Выйти.
""")
### Body
text1()
anq = raw_input("Выберите пункт для продолжения: ")
while anq != "Q" and anq != "q":
    text2()
    qwe = raw_input("Выберите пункт для продолжения: ")
    while qwe != "Q" and qwe != "q":
        if anq == "1":
            vibor_ip()
        elif anq == "2":
            vibor_ip_tren()
        if qwe == "1":
            stop_vektor()
        elif qwe == "2":
            start_vektor()
        elif qwe == "3":
            restart_vektor()
        elif qwe == "4":
            ftp_ok()
            if item == "L" and item == "l":
                download()
                stop_vektor()
                obnova()
                start_vektor()
                dostup()
            elif item == "Y" and item == "y":
                stop_vektor()
                obnova()
                start_vektor()
                dostup()
        elif qwe == "0":
            download()
        os.system('sleep 2')
        text2()
        qwe = raw_input("Выберите пункт для продолжения: ")
    os.system('sleep 2')
    text1()
    anq = raw_input("Выберите пункт для продолжения: ")
