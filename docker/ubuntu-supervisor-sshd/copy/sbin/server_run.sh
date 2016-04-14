#!/bin/bash

/sbin/link_mutable_files.py

if [ -e /sbin/prepare-magic.sh ]
then
    bash /sbin/prepare-magic.sh
fi

/usr/bin/supervisord
