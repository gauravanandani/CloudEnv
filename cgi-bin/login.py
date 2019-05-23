#!/usr/bin/python3.6

import os
import cgi
import mysql.connector as mariadb

print("Content-Type:text/html")
print("")
web=cgi.FieldStorage()

email=web.getvalue('email')
password=web.getvalue('password')
#email='abc@gmail.com'
#password='123'


conn=mariadb.connect(user='root', password='redhat', database='cloudvm')
cursor=conn.cursor()

cursor.execute("select email,password from registration where email='"+str(email)+"' and password='"+str(password)+"'")
a=cursor.fetchall()

try:
	if(a[0][0]!=email or a[0][1]!=password):
		print("<script>")
		print("alert('Invalid Credentials');")
		print("</script>")
		print("<meta http-equiv=refresh content=0;url=/login.html />")
	else:
		cursor.execute("select name,port,port2 from registration where email='"+str(email)+"'")
		data=cursor.fetchall()
		f=open("files/redhatport","w")
		f.write(""+str(data[0][1])+"")
		f.close()
		f1=open("files/ubuntuport","w")
		f1.write(""+str(data[0][2])+"")
		f1.close()
		print("<script>")
		print("alert('Welcome "+str(data[0][0])+"...');")
		print("</script>")
		print("<meta http-equiv=refresh content=0;url=/services.html />")
except:
	print("<script>")
	print("alert('Invalid Credentials');")
	print("</script>")
	print("<meta http-equiv=refresh content=0;url=/login.html />")


conn.close()
