FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y nginx
RUN apt-get install -y zabbix-server-pgsql zabbix-frontend-php
RUN apt-get remove -y postgresql postgresql-9.5


COPY copy/etc/supervisor/conf.d/zabbix.conf /etc/supervisor/conf.d
COPY authorized_keys /root/.ssh

RUN mkdir /var/run/nginx
RUN mkdir /run/php

#COPY copy/sbin/prepare_magic.sh /sbin
#RUN chmod a+x /sbin/prepare_magic.sh

COPY copy/etc/zabbix/zabbix_server.conf /etc/zabbix
#COPY of frontend conf file after postgres 
#COPY copy/etc/php5/php-fpm.conf /etc/php5
#COPY copy/etc/php5/php.ini /etc/php5
COPY copy/etc/nginx/nginx.conf etc/nginx
COPY copy/etc/nginx/cert.pem etc/nginx
COPY copy/etc/nginx/cert.key etc/nginx

VOLUME ["/var/log"]

EXPOSE 443
