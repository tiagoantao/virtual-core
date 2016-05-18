FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add sqlite
RUN apk add php5-fpm nginx php5-openssl php5-sqlite3 php5-sysvsem
RUN apk add zabbix zabbix-sqlite zabbix-webif zabbix-setup


COPY copy/etc/supervisor.d/zabbix.ini /etc/supervisor.d
#COPY authorized_keys /root/.ssh

RUN mkdir /var/run/nginx

COPY copy/sbin/prepare_magic.sh /sbin
RUN chmod a+x /sbin/prepare_magic.sh

COPY copy/etc/zabbix/zabbix_server.conf /etc/zabbix
#COPY of frontend conf file after postgres 
COPY copy/etc/php5/php-fpm.conf /etc/php5
COPY copy/etc/php5/php.ini /etc/php5
COPY copy/etc/nginx/nginx.conf etc/nginx
COPY copy/etc/nginx/cert.pem etc/nginx
COPY copy/etc/nginx/cert.key etc/nginx

VOLUME ["/var/log"]

EXPOSE 443
