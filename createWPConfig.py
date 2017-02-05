#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import subprocess
from subprocess import Popen,PIPE
import passwd
import init
import codecs

"""read sample config file, each line write to config file and rewrite only
the ones which are related to database settings. Then copy the config file 
to the /var/www/ directory  IBAN: GR02 0172 0360 0050 3605 5747 230"""

DBNAME="DB_NAME"
DBUSER="DB_USER"
DBPASSWD="DB_PASSWORD"

def wpConfig(curWPDir,homeDir,x):
	
	readFileHandler=codecs.open(curWPDir+"/"+init.sampleConfigFile,"r")
	currentDir=os.getcwd()
	os.chdir(homeDir)
	currentDir=os.getcwd()
	print currentDir
	writeFileHandler=codecs.open(homeDir+"/"+init.configFile,'w')
	"""writeFileHandler=open(curWPDir+"/"+init.configFile,"w+")"""
	
	
	line=readFileHandler.readline()

	while True:
		print line
		
		if line.find(DBNAME):
			writeLine="define('"+DBNAME+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine+"\n")
			print writeLine
			
		elif line.find(DBUSER):
			writeLine="define('"+DBUSER+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine+"\n")
			print writeLine
			
		elif line.find(DBPASSWD):
			writeLine="define('"+DBPASSWD+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine+"\n")
			print writeLine
			
		else:
			print line
			writeFileHandler.write(line+"\n")
			print line
			
		line=readFileHandler.readline()

		if line=='':
			break
		
	readFileHandler.close()
	writeFileHandler.close()
