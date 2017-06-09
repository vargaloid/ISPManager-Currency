#!/usr/bin/python

import MySQLdb
import string

#Connect to database
db = MySQLdb.connect(host="localhost", user="---DB_USERNAME---", passwd="---USERNAME_PASSWORD---", db="---DB_NAME---", charset='utf8')
#Cursor
cursor = db.cursor()

#Request to DB
uah = "SELECT rate FROM currencyrate WHERE currency_base=153 AND currency_relate=151 AND DATE(ratedate)=DATE(now());"
eur = "SELECT rate FROM currencyrate WHERE currency_base=153 AND currency_relate=50 AND DATE(ratedate)=DATE(now());"
#Get request
cursor.execute(uah)
uah = cursor.fetchall()
cursor.execute(eur)
eur = cursor.fetchall()

for E in eur:
	eur=E[0]
for H in uah:
	uah=H[0]

#Make file
make_file = open('currency_rate_today.php', 'w')
file_data = "<?php\n$eur=%s;\n$uah=%s;\n$usd=1;\n?>" % (eur, uah)
make_file.write(file_data)

#Close db connect
db.close()
