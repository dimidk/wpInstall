#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import subprocess
from subprocess import Popen,PIPE
import passwd
import init
import createWPConfig

mysql_user="; CREATE USER '"+init.baseDir+"wp"
mysql_userAppend="'@'localhost' identified by '"+init.baseDir+"wp"
mysql_grant="'; GRANT ALL PRIVILEGES ON "+init.baseDir+"wp"
mysql_grantAppend=".* to '"+init.baseDir+"wp"

chown_cmd=init.chown_CMD+"/wordpress"
chmod_cmd=init.chmod_CMD+"/wordpress"

def callCommand(cmd):
	
	if (subprocess.call(cmd))==0:
		print "Ok"
	else:
		print "Error in",cmd," command"
		exit(0)
		

curDir=os.getcwd()
homeDir=curDir
os.chdir(init.installDir)
curDir=os.getcwd()
if (curDir==init.installDir):
	print "you are in the correct directory"
else:
	print "You are in wrong directory"
	exit(0)
	
for x in range(init.number_install):
	
	callCommand(init.tarcmd.split(' '))
	callCommand(chown_cmd.split(' '))
	callCommand(chmod_cmd.split(' '))
	
	mv_cmd=init.mv_CMD+str(x)
	
	callCommand(mv_cmd.split(' '))
		
	
	mysql_cmd=init.mysql_CMD
	
	mysql_cmd=mysql_cmd+str(x)+mysql_user+str(x)+mysql_userAppend+str(x)+mysql_grant+str(x)+mysql_grantAppend+str(x)+"'@'localhost'\""
	
	print mysql_cmd.split('"')[1]
	p=subprocess.Popen(mysql_cmd,stdout=subprocess.PIPE,shell=True)

	p.communicate("exit")
	if p.returncode==0:
		print "Ok"
	else:
		print "database error"
		exit(0)
	
	mysql_cmd=""
	
for x in range(init.number_install):
	
	curWPDir=init.installDir+"/wp"+str(x)
	createWPConfig.wpConfig(curWPDir,homeDir,x)
	
	
	cp_cmd="sudo cp "+init.configFile+" "+init.installDir+"/wp"+str(x)
	mvfile_cmd="sudo cp " + init.installDir+"/wp" + str(x)+"/"+init.configFile +" "+init.installDir+"/wp" + str(x)+"/"+init.sampleConfigFile
	callCommand(cp_cmd.split(' '))

	curDir=os.getcwd()
	print curDir
	
	chown_cmd=init.chown_CMD+"/wp"+str(x)
	chmod_cmd=init.chmod_CMD+"/wp"+str(x)
	
	callCommand(chown_cmd.split(' '))
	callCommand(chmod_cmd.split(' '))
	callCommand(mvfile_cmd.split(' '))
	
	
	
	
		
	
	
	
	
