#!/bin/bash

nf=`ls /var/lib/postgresql |wc -w`
if [ $nf -eq 0 ]; then
  mkdir /var/lib/postgresql/data
  chown postgres.postgres /var/lib/postgresql/data
  sudo -u postgres -g postgres initdb /var/lib/postgresql/data/
  sudo -u postgres -g postgres cp /copy/var/lib/postgresql/data/* /var/lib/postgresql/data/
else
  echo "will not build";
fi
