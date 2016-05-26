#!/bin/bash


apt-get install -y postgresql-server-dev-9.5
apt-get install -y build-essential libsnmp-dev

wget http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Stable/3.0.3/zabbix-3.0.3.tar.gz/download -O zabbix-3.0.3.tar.gz

tar zxf zabbix-3.0.3.tar.gz
cd zabbix-3.0.3
./configure --enable-server --with-postgresql --with-net-snmp
make install
mkdir -p /usr/local/web/zabbix
cp -r frontends/php/* /usr/local/web/zabbix
mkdir /db
cp database/postgresql/* /db
cd ..
rm -rf zabbix-3.0.3*


apt-get remove -y postgresql-server-dev-9.5
apt-get remove -y build-essential g++ gcc dpkg-dev perl libsnmp-dev
apt-get autoremove -y
apt-get clean
