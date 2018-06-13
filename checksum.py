# -*- coding: utf8 -*-
import os, hashlib, threading
from datetime import datetime
from threading import Thread

path='/home/derokhin'
need_format='README'

def check_sum(filo):
    doc = str("sum.txt")
    fout = open(doc, 'a')
    tiktak = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    text = "{}\n{}".format(filo, tiktak)
    print(text, file=fout)
    hash = hashlib.md5(open(filo,'rb').read()).hexdigest()
    tiktak = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    text = "{}\n{}\n------".format(tiktak, hash)
    print(text, file=fout)
    fout.close()

for rootdir, dirs, files in os.walk(path):
    for file in files:
        if((file.split('.')[-1])==need_format):
            filo = os.path.join(rootdir, file)
            t = Thread(target=check_sum, args=(filo,))
            t.start()
