#!/usr/bin/python
#-*- coding: utf-8 -*-

"""mysql -Bse : -B batch work, not interactive -s silent mode -e execute command"""

import passwd


wordpress="/var/www/ALykeiou/wordpress-4.7.1-el.tar.gz"
baseDir="ALykeiou"
installDir="/var/www/"+baseDir
tarcmd="sudo tar -xvf "+wordpress

mysqlDict={'user':passwd.userName,'password':passwd.password,'host':passwd.hostName}
mysql_CMD="mysql --user={user} --password={password} -Bse \"""CREATE DATABASE "+baseDir+ "wp".format(**mysqlDict)
chown_CMD="sudo chown www-data:www-data -R "+installDir
chmod_CMD="sudo chmod 755 -R " +installDir
mv_CMD="sudo mv "+installDir+"/wordpress "+installDir+"/wp"




