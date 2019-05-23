#!/usr/bin/python3.6
from subprocess import Popen as process
from subprocess import PIPE as pipe

print("Content-Type:text/html")
print("")

f=open("files/redhatport","r")
i=f.read()

if(i=="None"):
	print("<meta http-equiv=refresh content=0;url=/redhatvm.html />")
else:
	a=process("ls /var/lib/libvirt/images/redhat"+str(i)+".qcow2",shell=True,stdout=pipe)
	b=a.stdout.readline()
	try:
		if(b[0]==47):
			print("<script>")
			print("alert('You had already built your Instance.!! Click OK to continue that..');")
			print("</script>")
			print("<meta http-equiv=refresh content=0;url=/cgi-bin/existvmsredhat.py />")
		else:
			print("<meta http-equiv=refresh content=0;url=/redhatvm.html />")
	except:
		print("<meta http-equiv=refresh content=0;url=/redhatvm.html />")
