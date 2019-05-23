#!/usr/bin/python

import  cgi
import commands

#Getting Value...
print ("Content-type:text/html")
print  ("")
web=cgi.FieldStorage()
c=web.getvalue('t1')

print('''
<html>
<head>
<link rel="stylesheet" href="/css/bootstrap.min.css">
<script>
function blank()
{
var a=document.forms["f1"]["t1"].value;
if(a == "")
{
alert("Please Enter any command to execute");
return false;
}
}
</script>
</head>
<body>
<form name="f1"  action="/cgi-bin/paas/paas.py" onsubmit="return blank()">
<div class="container">
	<div class="jumbotron" style="background-image: url('/paasbg.png');">
		<h1>Welcome to PAAS Plateform</h1>	
	<div class="form-group">
		<input type=text name="t1" placeholder="Please Enter your command to execute" class=form-control>
	</div>
		<input type=submit value="Click Me" class="btn btn-default"><br/><br/>
		<a href=/index.html>Go Home</a>
	</div>

</div>
</form>
</body>
</html>
''')


print ("<pre>")
print ("Output:-")
a=c
print(commands.getoutput(a))
#a=commands.getoutput("docker run ubuntu "+str(a)+"")
#print(a)
print ("</pre>")
