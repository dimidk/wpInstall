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
to the /var/www/ directory """


AUTH_KEY="define('AUTH_KEY',         '#&y$@^N-uR2m:,}~5y><J?c&fyNk0+$Lk(Qz|l:l|m/fr| YR84Kb7pzf@4aC`Cl');"
SECURE_AUTH_KEY="define('SECURE_AUTH_KEY',  'o2B:%2_D-5+>}r$)f8-nr<m]^wmbf/6=_m]wR*.5sH6^U{GaUgr~PG`j%1<7o]Mt');"
LOGGED_IN_KEY="define('LOGGED_IN_KEY',    '>L_!J+>TBnCi)y]Z.M-v4.t|HEl/!yj903]2sa(F~JwZ8$cTK]Y`~t{-z5+#?tP>');"
NONCE_KEY="define('NONCE_KEY',        '02U7xl&P&7BF<.bzp@S{j7VEL%e^<[YGPU?X<~XH/sH-^Zcik_A_wD%wukyahg2x');"
AUTH_SALT="define('AUTH_SALT',        'E6yiwA51W^$nb([FMb:8+btm_.i--J(.>eMrjOb)3#n43^5!#Lr4]g`+-x(4b6;k');"
SECURE_AUTH_SALT="define('SECURE_AUTH_SALT', 'aikPT]:q@UCC.1-9BIk-?QdCHyO||IwP)B9hM2Vk!2p{?`(* >qk!xs0$/~p5_I;');"
LOGGED_IN_SALT="define('LOGGED_IN_SALT',   '5eE(,a&MG.Vvr|Ne3HBg*7V(l4NpWDaOlZdZffex+,`}Ei,]s3h3EWV)&I0Whk|[');"
NONCE_SALT="define('NONCE_SALT',       '%~K7hi>Fs#+6*]+ef2zj}VV$v-l3PYF>P}>93H~v0;~Sl~o4-{Ipe9X|Q;>Zj#p-');"



""" add the above to file to continue with installation"""

DBNAME="DB_NAME"
DBUSER="DB_USER"
DBPASSWD="DB_PASSWORD"
DB_COLLATE="DB_COLLATE"

def wpConfig(curWPDir,homeDir,x):
	
	readFileHandler=codecs.open(curWPDir+"/"+init.sampleConfigFile,"r")
	
	currentDir=os.getcwd()
	os.chdir(homeDir)
	currentDir=os.getcwd()
	print currentDir
	writeFileHandler=codecs.open(homeDir+"/"+init.configFile,'w')
	
	line=readFileHandler.readline()

	while True:
		
		if line.find(DBNAME)!=-1:
			print "I am in dbname"
			writeLine="define('"+DBNAME+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine)
			print writeLine
			
		elif line.find(DBUSER)!=-1:
			print "I am in dbuser"
			writeLine="define('"+DBUSER+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine)
			print writeLine
			
		elif line.find(DBPASSWD)!=-1:
			print "I am in dbpasswd"
			writeLine="define('"+DBPASSWD+"', '"+init.baseDir+"wp"+str(x)+"')"
			writeFileHandler.write(writeLine)
			print writeLine
		
		elif line.find(DB_COLLATE)!=-1:
			print "I am in dbcollate"
			writeFileHandler.write(line)
		elif line.find('AUTH_KEY')!=-1:

			writeFileHandler.write(AUTH_KEY+"\n")
		elif line.find('SECURE_AUTH_KEY')!=-1:
			
			writeFileHandler.write(SECURE_AUTH_KEY+"\n")
		elif line.find('LOGGED_IN_KEY')!=-1:
			
			writeFileHandler.write(LOGGED_IN_KEY+"\n")
		elif line.find('NONCE_KEY')!=-1:
			
			writeFileHandler.write(NONCE_KEY+"\n")
		elif line.find('AUTH_SALT')!=-1:
			
			writeFileHandler.write(AUTH_SALT+"\n")
		elif line.find('SECURE_AUTH_SALT')!=-1:	
			
			writeFileHandler.write(SECURE_AUTH_SALT+"\n")
		elif line.find('LOGGED_IN_SALT')!=-1:
			
			writeFileHandler.write(LOGGED_IN_SALT+"\n")
		elif line.find('NONCE_SALT')!=-1:
			
			writeFileHandler.write(NONCE_SALT+"\n")
			
		else:
			print line
			writeFileHandler.write(line)
			print line
			
			
		line=readFileHandler.readline()

		if line=='':
			break
		
	readFileHandler.close()
	writeFileHandler.close()
