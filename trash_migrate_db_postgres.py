#!/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
from subprocess import Popen, PIPE
# Основной
serverdb101 = str("10.32.5.10") # isuz-orcl-101
serverdb102 = str("10.32.5.20") # isuz-orcl-102
servermain101 = str("10.32.5.11") # isuz-main-101
servermain102 = ("10.32.5.21") # isuz-main-102
# Тренажерный
serverdb201 = str("10.32.5.30") # isuz-orcl-201
serverdb202 = str("10.32.5.40") # isuz-orcl-202
servermain201 = str("10.32.5.31") # isuz-main-201
servermain202 = str("10.32.5.41") # isuz-main-202
# Трешка
serverdb301 = str("10.35.33.10") # orcl-301
serverdb302 = str("10.35.33.20") # orcl-302
servermain301 = str("10.35.33.11") # main-301
servermain302 = str("10.35.33.21") # main-302
# Нижегородка
server186 = str("10.160.22.186")
server188 = str("10.160.22.188")

os.system('clear')
print """Что делать?
1 - скопировать
2 - установить дамп"""
qwe = raw_input()
if qwe == "1":
	print ("Откуда?")
	print ("1 - " + serverdb101 )
	print ("2 - " + serverdb301)
	print ("3 - " + serverdb302 )
	asd = raw_input()
	if asd == "1":
		bd_2 = serverdb101
	elif asd == "2":
		bd_2 = serverdb301
	elif asd == "3":
		bd_2 = serverdb302
	print ("Куда?")
	print ("1 - " + serverdb301)
	print ("2 - " + serverdb302)
	print ("3 - " + server186)
	print ("4 - " + server188)
	zxc = raw_input()
	if zxc == "1":
		bd_1 = serverdb301
	elif zxc == "2":
		bd_1 = serverdb302
	elif zxc == "3":
		bd_1 = server186
	elif zxc == "4":
		bd_1 = server188
	print ("Находим последний дамп на " + bd_2 + "\n")
	options = Popen('ssh root@' + bd_2 + ' "find /u02/scripts_imp_exp/datapump/impdp_expdp/dump/export-dp/ -type f -ctime -5 | sort -r"', shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
	print(options)
	damp = input("\nВыбери нужный дамп: ")
	print ("\nКопируем с " + bd_2 + " на ПК в /opt/damp/\n")
	os.system("scp "+ bd_2 + ":" + options[damp] + " /opt/damp/")
	print ("Копируем с ПК на " + bd_1 + " в /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/\n")
	os.system("scp /opt/damp/* " + bd_1 + ":/u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/")
	os.system("ssh root@" + bd_1 + " \"cd /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp; chown oracle:oinstall ./*\"")
	os.system("rm -rf /opt/damp/*")
	rty = raw_input("Разархивировать дамп? ")
	if rty == "Y" or rty == "y":
		options = Popen('ssh root@' + bd_1 + ' "find /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/ -type f -ctime -1 | sort -r | head -5"', shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
		print(options)
		damp = raw_input("Выбери нужный архив:")
		os.system("scp "+ bd_2 + ":" + options[damp] + " /opt/damp/")
		if qwe == "1":
			os.system("cd /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/; tar -xvjf " + options[damp])
		else:
			os.system("cd /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/; tar -xvzf " + options[damp])
		print("Результат:")
		os.system('ssh root@' + bd_1 + '" cd /u02/scripts_imp_exp/datapump/impdp_expdp/dump/import-dp/; ls -l | sort -r | head -5"')
	else:
		print("Дамп разархивировать не будем.\n")
elif qwe == "2":
	print("не готово.\n")
