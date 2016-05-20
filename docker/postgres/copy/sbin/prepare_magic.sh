#!/bin/bash

#this is for alpine linux, irrelevant with debian/ubuntu
nf=`ls /var/lib/postgresql |wc -w`
if [ $nf -eq 0 ]; then
  mkdir /var/lib/postgresql/data
  chown postgres.postgres /var/lib/postgresql/data
  sudo -u postgres -g postgres initdb /var/lib/postgresql/data/
  sudo -u postgres -g postgres cp /copy/var/lib/postgresql/data/* /var/lib/postgresql/data/
else
  echo "will not build";
fi

#this is for all, will fail after first exec - not problematic
sudo -u postgres -g postgres createuser zabbix
sudo -u postgres -g postgres createdb -O zabbix zabbix
