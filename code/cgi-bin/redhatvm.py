#!/usr/bin/python3.6

import os
import cgi
import mysql.connector as mariadb
import time
import subprocess


print("Content-type:text/html")
print("")

web=cgi.FieldStorage()

ram=web.getvalue('ram')
cpu=web.getvalue('cpu')
#port=web.getvalue('port')

conn=mariadb.connect(user='root', password='redhat', database='cloudvm')
cursor=conn.cursor()

print ("<meta http-equiv=refresh content=0;url=/cgi-bin/existvmsredhat.py/>")
#auto assign port
cursor.execute("select port from portinc order by port desc")
a=cursor.fetchone()
cursor.fetchall()
r=a[0] 
#print (q)
if(a!=None):
	p=r+1
	try:
		cursor.execute("INSERT INTO portinc (port) VALUES ("+str(p)+")")
	except mariadb.Error as error:
		print("Error:{}",format(error))
	conn.commit()	

#checking &&& inserting port
cursor.execute("select id from inc order by id desc")
b=cursor.fetchone()
cursor.fetchall()
q=b[0]
#print (q)
if(b!=None):
	i=q+1
	f=open("files/redhatport","w")
	f.write(""+str(i)+"")	
	f.close()
	try:
		cursor.execute("INSERT INTO inc (id) VALUES ("+str(i)+")")
	except mariadb.Error as error:
		print("Error:{}",format(error))
	conn.commit()

#link port with email	
f1=open("files/email","r")
email=f1.read()
cursor.execute("update registration set	port='"+str(i)+"' where email='"+str(email)+"'")
conn.commit()
conn.close()

print(" Please Wait your Instance is building...")

#building process
subprocess.Popen("sudo qemu-img  create -f qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/redhat"+str(i)+".qcow2 ",shell=True,stdout=subprocess.PIPE)

f1=open("files/psd","r")
p=f1.read()
subprocess.Popen("sudo virt-install --name redhat"+str(i)+" --ram "+str(ram)+" --vcpu "+str(cpu)+" --disk path=/var/lib/libvirt/images/redhat"+str(i)+".qcow2 --import --graphics=vnc,listen=127.0.0.1,port="+str(r)+",password="+str(p)+" --noautoconsole  &",shell=True,stdout=subprocess.PIPE)


subprocess.Popen("nohup websockify --web=/usr/share/novnc "+str(i)+" 127.0.0.1:"+str(r)+"  &",shell=True)



