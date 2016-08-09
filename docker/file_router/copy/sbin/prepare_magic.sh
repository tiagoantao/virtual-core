#!/bin/bash

while read name id passwd; do
    useradd "$name" -M -u "$id"
    printf "${passwd}\n${passwd}\n" | pdbedit -a -u "$name" -t 
done < <(cut -f1,2,3 --output-delimiter=' ' /etc/samba/users)
#mv /etc/samba/users /etc/samba/users.done
