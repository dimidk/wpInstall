#!/usr/bin/python
#-*- coding: utf-8 -*-

"""mysql -Bse : -B batch work, not interactive -s silent mode -e execute command"""

import passwd

number_install=20
wordpress="/var/www/ALykeiou/wordpress-4.7.1-el.tar.gz"
baseDir="ALykeiou"
installDir="/var/www/"+baseDir

sampleConfigFile="wp-config-sample.php"
configFile="wp-config.php"

tarcmd="sudo tar -xvf "+wordpress
mysqlDict={'user':passwd.userName,'password':passwd.password,'host':passwd.hostName}
mysqlcmd="mysql --user={user} --password={password} -Bse \"""CREATE DATABASE "+baseDir+ "wp"
mysql_CMD=mysqlcmd.format(**mysqlDict)
chown_CMD="sudo chown www-data:www-data -R "+installDir
chmod_CMD="sudo chmod 755 -R " +installDir
mv_CMD="sudo mv "+installDir+"/wordpress "+installDir+"/wp"
cp_config="sudo cp " 

dropcmd="mysql --user={user} --password={password} -Bse \"""DROP DATABASE "+baseDir+ "wp"
drop_CMD=dropcmd.format(**mysqlDict)
drop_user="; DROP USER '"+baseDir+"wp"
rm_CMD="sudo rm -r "+installDir+"/wp"



