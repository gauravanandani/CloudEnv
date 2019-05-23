#!/usr/bin/python3.6


import os
import cgi
import time
import mysql.connector as mariadb


print("Content-Type:text/html")
print("")

web=cgi.FieldStorage()


name=web.getvalue('name')
email=web.getvalue('email')
password=web.getvalue('password')
#email='gauravanandani@gmail.com'
conn=mariadb.connect(user='root', password='redhat', database='cloudvm')
cursor=conn.cursor()
cursor.execute("select email from registration where email='"+str(email)+"'")
a=cursor.fetchone()
if(a!=None):
	if(a[0]==email):
		print("<script>")
		print("alert('User already Exist Try to login...');")
		print("</script>")	
		print("<meta http-equiv=refresh content=0;url=/login.html />")
else:
	try:
		cursor.execute("INSERT INTO registration (name,email,password) VALUES(%s,%s,%s)",(name,email,password))
		conn.commit()
		print("<script>")
		print("alert('Signup Successfully done!! Now You Need To Login...');")
		print("</script>")
		print("<meta http-equiv=refresh content=0;url=/login.html />")
		f=open("files/psd","w")
		f.write(""+str(password)+"")
		f.close()
		f1=open("files/email","w")
		f1.write(""+str(email)+"")
		f1.close()
	except mariadb.Error as error:
		print("Error:{}",format(error))

conn.close()
#exec(open('existredhat.py').read())

