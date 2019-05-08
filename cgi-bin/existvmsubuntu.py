#!/usr/bin/python3.6

import os
import cgi
import mysql.connector as mariadb
import subprocess

print("Content-Type:text/html")
print("")
web=cgi.FieldStorage()

#email='abc@gmail.com'
#password='123'


#		print("<meta http-equiv=refresh content=0;url=/cgi-bin/existvms.py />")



print(
"""
<html>
<head>
<link rel="stylesheet" href="/css/bootstrap.min.css"/>
        <link rel="stylesheet" href="/css/font-awesome.min.css"/>
        <link rel="stylesheet" href="/css/magnific-popup.css"/>
        <link rel="stylesheet" href="/css/owl.carousel.min.css"/>
        <link rel="stylesheet" href="/css/style.css"/>
        <link rel="stylesheet" href="/css/animate.css"/>
</head>
<body>

<!-- Header section -->
        <header class="header-section">
                <div class="container">
                        <h4>
                        <a href="index.html">
                        Cloud Env.
                        </a>
                        </h4>
                        <!-- Switch button -->
                        <div class="nav-switch">
                                <div class="ns-bar"></div>
                        </div>
                        <div class="header-right">
                                <ul class="main-menu">
                                        <li class="active"><a href="/index.html" class="site-btn sb-c1">HOME</a></li>
                                        <li><a href="#"class="site-btn sb-c2">Support</a></li>
                                        <li><a href="/index.html" class="site-btn sb-c3">Logout</a></li>
                                        <li><a href="/cgi-bin/services.py" class="site-btn sb-c4">Goto Main Page</a></li>
                                </ul>
                        </div>

                </div>
        </header>
        <!-- Header section end -->


<br/><br/><br/><br/><br/><br/><br/>

<form class="form-horizontal" action=existvmsubuntu.py method='POST'>
<div class="container">
<div class="jumbotron">
<center><h1>UBUNTU OS</h1></center>
</div>

<div class="container">
 <div class="col-md-4">
  <label class="col-md-4 control-label">PowerUp</label>
  <input type=radio name='control' value='pu'>
 </div>
 <div class="col-md-4">
  <label class="col-md-4 control-label">PowerOff</label>
  <input type=radio name='control' value='po'>
 </div>
 <div class="col-md-4">
  <label class="col-md-4 control-label">Restart</label>
  <input type=radio name='control' value='rs'>
 </div>
<br/><br/>
 <div class="col-md-3">
  <label class="col-md-3 control-label">Reset</label>
  <input type=radio name='control' value='res'>
<br/><font color="red"><b>Caution: If you reset your Instance your saved data will be removed.</b></font>
 </div>
</div>
<br/>
<br/><br/>
<input type=submit value=Submit>
</body>
</html>
""")
option=web.getvalue('control')
f=open('files/ubuntuport','r')
port=f.read()

if(port=="None"):
	print("<script>")
	print("alert('You Dont have any OS first build..');")
	print("</script>")
	print("<meta http-equiv=refresh content=0;url=/iaaschoose.html />")
else:
	if(option=='pu'):
		pu=subprocess.Popen("sudo virsh start ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
		pu2=pu.stdout.readline()
		if(pu2==" b'\n'"):
			print("<script>")
			print("alert('OS already On');")
			print("</script>")
	elif(option=='po'):
		po=subprocess.Popen("sudo virsh destroy ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
		po2=po.stdout.readline()
	elif(option=='rs'):
		subprocess.Popen("sudo virsh destroy ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
		subprocess.Popen("sudo virsh start ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
	elif(option=='res'):
		subprocess.Popen("sudo virsh start ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
		subprocess.Popen("sudo virsh reset ubuntu"+str(port)+"",shell=True,stdout=subprocess.PIPE)
print("<br/><br/>")
print("Status:")
ab=subprocess.Popen("sudo virsh domcontrol ubuntu"+str(port)+" &",shell=True,stdout=subprocess.PIPE)
ba=ab.stdout.readline()
if(ba[0]==111):
	print("<font color='green'>Poweron</font>")
	print("<a href=/cgi-bin/existvmsubuntu.py>Recheck</a>")
	print("<h3><a target='_blank'  href=http://127.0.0.1:"+str(port)+">Click Here to go to access your Instance</a></h3>")
else:
	print("<font color='red'>Poweroff</font>")
	print("<a href=/cgi-bin/existvmsubuntu.py>Recheck</a>")



'''
	print (s)
		if(s!=0):
			print("<script>")
			print("alert('OS already On');")
			print("</script>")
			print ("<meta http-equiv=refresh content=0;url=http://192.168.42.192:"+str(a[0][0])+" />")
		else:
			print("Content-Type: text/html")
			print ("<meta http-equiv=refresh content=2;url=http://192.168.42.192:"+str(a[0][0])+" />")
else:
	print("<script>")
	print("alert('User does not Exist');")
	print("</script>")
	print ("<meta http-equiv=refresh content=0; url=/ubuntuvm.html />")
'''
