#!/bin/bash

if [ ! -e /db/zabbix.sqlite ]
then
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/schema.sql;
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/images.sql;
   sqlite3 /db/zabbix.sqlite < /usr/share/zabbix/database/sqlite3/data.sql
fi

