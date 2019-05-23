#!/usr/bin/python3.6
from subprocess import Popen as process
from subprocess import PIPE as pipe

print("Content-Type:text/html")
print("")

f=open("files/ubuntuport","r")
i=f.read()

if(i=="None"):
	print("<meta http-equiv=refresh content=0;url=/ubuntuvm.html />")
else:
	a=process("ls /var/lib/libvirt/images/ubuntu"+str(i)+".qcow2",shell=True,stdout=pipe)
	b=a.stdout.readline()
	try:
		if(b[0]==47):
			print("<script>")
			print("alert('You had already built your Instance.!! Click OK to continue that..');")
			print("</script>")
			print("<meta http-equiv=refresh content=0;url=/cgi-bin/existvmsubuntu.py />")
		else:
			print("<meta http-equiv=refresh content=0;url=/ubuntuvm.html />")
	except:
		print("<meta http-equiv=refresh content=0;url=/ubuntuvm.html />")





