#!/usr/bin/env python
# coding: utf8

import psycopg2

dbhost = '{{host_portal_db}}'
dbname = 'lportal2'
dbuser = 'lportal'
dbpass = '{{portal_db_pass}}'

val_from = 'https://url_old'
val_to = 'https://url_new'

try:
    conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (dbname, dbuser, dbhost, dbpass))
except:
    print "I am unable to connect to the database: %s" % dbhost

cur = conn.cursor()
cur.execute("""select layoutsetid, settings_ from layoutset""")

rows = cur.fetchall()

for row in rows:
    key = row[0]
    val_origin = row[1]
    val_new = val_origin.replace(val_from, val_to)
    print
    print '**********************************************************************'
    print 'KEY: %s' % key
    print 'ORIGIN VAL:'
    print val_origin
    print 'NEW VAL:'
    print val_new
    sql = """update layoutset set settings_ = '%s' where layoutsetid = %d ;""" % (val_new, key)
    print 'SQL:'
    print sql
    cur_update = conn.cursor()
    cur_update.execute(sql)

conn.commit()
