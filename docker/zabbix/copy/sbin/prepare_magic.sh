#!/bin/bash

if [ ! -e /var/log/zabbix ]
then
    mkdir /var/log/zabbix;
    chown zabbix.zabbix /var/log/zabbix
    mkdir /var/log/nginx;
fi

if [ ! -e /db/zabbix.sqlite ]
then
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/schema.sql;
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/images.sql;
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/data.sql
   chown zabbix.zabbix /db/zabbix.sqlite
fi

