#!/bin/bash

if [ -e /sbin/prepare-magic.sh ]
then
    bash /sbin/prepare-magic.sh
fi
/usr/bin/supervisord
