FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add sqlite
RUN apk add php5-fpm nginx php5-openssl
RUN apk add zabbix zabbix-sqlite zabbix-webif zabbix-setup


#COPY copy/etc/supervisor.d/phpldap.ini /etc/supervisor.d
#COPY authorized_keys /root/.ssh

RUN mkdir /db; chown zabbix.zabbix /db

COPY copy/sbin/prepare_magic.sh /sbin
RUN chmod a+x /sbin/prepare_magic.sh

COPY copy/etc/zabbix/zabbix_server.conf /etc/zabbix
COPY copy/etc/php/php-fpm.conf /etc/php

VOLUME ["/var/log", "/db" , "/etc/nginx"]

EXPOSE 443