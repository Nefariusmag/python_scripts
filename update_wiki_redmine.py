#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, requests, re
from datetime import datetime

import sys

API_KEY = '-'
REDMINE_URL = 'http://redmine.ru/projects/16/wiki/'
tag_application = {'TAG_CLASSIFIER_VIEW': 'classifier-view', 'TAG_GTAFO': 'afo', 'TAG_GTARM': 'gtarm',
                   'TAG_GTCLASSIFIER': 'classifier', 'TAG_GTCONTROL': 'control', 'TAG_GTDOWNLOAD': 'gtdownload',
                   'TAG_GTEXPGISEE': 'import-ps-ues-gisee', 'TAG_GTIMPXML': 'gtimpxml', 'TAG_GTONL': 'gtonl',
                   'TAG_GTONL_HANDSONTABLE': 'gtonl-handsontable', 'TAG_GTTECHNOLOGIST': 'gttechologist',
                   'TAG_GTTRANSPORT': 'gtransport', 'TAG_GTXML': 'gtxml', 'TAG_LOADSSB': 'loadssb',
                   'TAG_REGISTRATION': 'registration', 'TAG_SSO_SERVER': 'sso-server', 'TAG_TICKET': 'ticket',
                   'tag_vendor': 'vendor'}
stand_wiki_pages = {'REA_TEST': 'Тестовый_стенд_заказчика_(TEST)', 'PI': 'Стенд_приемочных_испытаний_(ПИ)',
                    'PK': 'Подготовки_контента_(ПК)', 'ZERO': 'Нулевой_стенд_(ZERO)',
                    'DKP': 'Стенд_разработки_и_тестирования_(DKP)'}

update_list = list(
    # tag for tag in tag_application.keys() if os.environ[tag] != 'release' and tag != 'TAG_GTONL_HANDSONTABLE')
    tag for tag in tag_application.keys())

# another default value
# if os.environ['TAG_GTONL_HANDSONTABLE'] != 'release':
#     update_list.append('TAG_GTONL_HANDSONTABLE')

# check if issue_id is set
if 'issue_id' in os.environ:
    issue_id = '#' + os.environ['issue_id']
else:
    issue_id = '#'
url = REDMINE_URL + stand_wiki_pages.get(os.environ['stand']) + '.xml'
# get wiki page from redmine
r = requests.get(url, headers={'X-Redmine-API-Key': API_KEY}, stream=True)
# substitute application versions and write to file
with open('wiki.xml', 'w', encoding='utf-8') as f:
    for line in r.iter_lines():
        line = line.decode('utf-8')
        for tag in update_list:
            # find and replace string with application version
            line = re.sub(r'\|\s' + tag_application[tag] + '\s.*',
                          '| {} | {} | {} | {}  |'.format(tag_application[tag], os.environ[tag],
                                                         datetime.now().strftime('%d.%m.%Y %H:%M'),
                                                         issue_id),
                          line)
        f.write(line+'\n')
# send new wiki page to redmine
with open('wiki.xml', encoding='utf-8') as f:
    data = f.read()
    data = data.encode(encoding='utf-8')
    r = requests.put(url, data=data, headers={'X-Redmine-API-Key': API_KEY, 'Content-Type': 'application/xml'})

if r.status_code != 200:
    print('Some problems during sending wiki page to redmine!')
    print('Status:{}'.format(r.status_code))
    print('Content:{}'.format(r.content))
    sys.exit(1)
