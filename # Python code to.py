import mysql.connector
import re

cnx = mysql.connector.connect(user='root', password='77277874',
                              host='127.0.0.1',
                              database='tel_db')
cursor = cnx.cursor()

# Python code to
# demonstrate readlines()
# Using readlines()
file1 = open('TeleDB_light.TXT', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
	count += 1
	####
	txt=line.strip()
	if txt=="":
		continue
	"""print(txt,type(txt))#########
	input('*')"""
	telid=0
	username=""
	phoneno=0
	try:
		telid =re.findall(r'{\'id\': (\d{1,10}),', txt)
		telid=telid[0]
		"""print(telid,type(telid))#########
		input('*')"""
	except:
		pass
	try:
		username=re.findall(r'\'username\': \'(.{0,32})\',', txt)
		username=username[0]
		"""print(username,type(username))#########
		input('*')"""
	except:
		pass
	try:
		phoneno =re.findall(r'\'phone\': \'(.*)\'}', txt)
		phoneno=phoneno[0]
		"""print(phoneno,type(phoneno))#########
		input('*')"""
	except:
		pass
	####
	print("Line{}: {}".format(count, line.strip()))
	"""print('reqis||||||||||',telid,username,phoneno)"""
	record=(telid,username,phoneno)
	cursor.execute('insert into main VALUES (%s,%s,%s)',record)
	cnx.commit()#thats makes u sure that query has been exiquted sucsesfully *******
	


cnx.close()