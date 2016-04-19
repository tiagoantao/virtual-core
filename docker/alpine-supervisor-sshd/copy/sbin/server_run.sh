#!/bin/bash

/sbin/link_mutable_files.py

if [ -e /sbin/prepare_magic.sh ]
then
    bash /sbin/prepare_magic.sh
fi

/usr/bin/supervisord
