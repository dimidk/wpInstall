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
	exit
	
for x in range(5):
	
	subprocess.call(init.tarcmd.split(' '))
	subprocess.call(chown_cmd.split(' '))
	subprocess.call(chmod_cmd.split(' '))
	mv_cmd=init.mv_CMD+str(x)
	
	subprocess.call(mv_cmd.split(' '))
	
	mysql_cmd=init.mysql_CMD
	print mysql_cmd
	mysql_cmd=mysql_cmd+str(x)+mysql_user+str(x)+mysql_userAppend+str(x)+mysql_grant+str(x)+mysql_grantAppend+str(x)+"'@'localhost'\""
	print mysql_cmd
	p=subprocess.Popen(mysql_cmd,stdout=subprocess.PIPE,shell=True)

	p.communicate("exit")
	mysql_cmd=""
	
	
	
