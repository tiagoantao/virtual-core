#!/bin/bash

/sbin/link_mutable_files.py

if [ -e /sbin/prepare_magic.sh ]
then
    bash /sbin/prepare_magic.sh
fi

#in the (probable) case /var/log is a VOLUME
if [ ! -e /var/log/supervisor ]; then
   mkdir /var/log/supervisor
   #a few extras
   mkdir /var/log/nginx
   mkdir /var/log/zabbix
   mkdir /var/log/uwsgi
fi

/usr/bin/supervisord
