#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import subprocess
from subprocess import Popen,PIPE
import passwd
import init

mysql_user="; CREATE USER 'wp"
mysql_userAppend="'@'localhost' identified by 'wp"
mysql_grant="'; GRANT ALL PRIVILEGES ON wp"
mysql_grantAppend=".* to 'wp"



chown_cmd=init.chown_CMD+"/wordpress"
chmod_cmd=init.chmod_CMD+"/wordpress"

curDir=os.getcwd()
os.chdir(init.installDir)
curDir=os.getcwd()
if (curDir==init.installDir):
	print "you are in the correct directory"
else:
	print "You are in wrong directory"
	exit(0)
	
for x in range(5):
	
	if (subprocess.call(init.tarcmd.split(' ')))==0:
		print "Ok"
	else:
		print "error in tar command"
		exit(0)
		
	if (subprocess.call(chown_cmd.split(' ')))==0:
		print "Ok"
	else:
		print "error in chown command"
		exit(0)
	if (subprocess.call(chmod_cmd.split(' ')))==0:
		print "Ok"
	else:
		print "error in chmod command"
		exit(0)
	mv_cmd=init.mv_CMD+str(x)
	
	if (subprocess.call(mv_cmd.split(' ')))==0:
		print "Ok"
	else:
		print "error in mv command"
		exit(0)
		
	mysql_cmd=init.mysql_CMD
	print mysql_cmd
	mysql_cmd=mysql_cmd+str(x)+mysql_user+str(x)+mysql_userAppend+str(x)+mysql_grant+str(x)+mysql_grantAppend+str(x)+"'@'localhost'\""
	print mysql_cmd
	p=subprocess.Popen(mysql_cmd,stdout=subprocess.PIPE,shell=True)

	
	p.communicate("exit")
	if p.returncode==0:
		print "Ok"
	else:
		print "database error"
		exit(0)
	mysql_cmd=""
	
	
	
