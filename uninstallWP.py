#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import subprocess
from subprocess import Popen,PIPE
import passwd
import init

curDir=os.getcwd()
os.chdir(init.installDir)
curDir=os.getcwd()

if (curDir==init.installDir):
	print "you are in the correct directory"
else:
	print "You are in wrong directory"
	exit(0)
	
for x in range(1):
	
		
	rm_cmd=init.rm_CMD+str(x)
	
	if (subprocess.call(rm_cmd.split(' ')))==0:
		print "Ok"
	else:
		print "error in rm command"
		exit(0)
		
	drop_cmd=init.drop_CMD
	
	drop_cmd=drop_cmd+str(x)+init.drop_user+str(x)+"'@'localhost'\""
	
	print drop_cmd.split('"')[1]
	p=subprocess.Popen(drop_cmd,stdout=subprocess.PIPE,shell=True)

	
	p.communicate("exit")
	if p.returncode==0:
		print "Ok"
	else:
		print "database error"
		exit(0)
	drop_cmd=""
	
	
	
