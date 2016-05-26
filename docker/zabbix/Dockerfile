FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y nginx php7.0 php7.0-bcmath php7.0-gd php7.0-xml php7.0-mbstring php7.0-pgsql libsnmp30


COPY get_zabbix_server.sh .
RUN bash get_zabbix_server.sh


COPY authorized_keys /root/.ssh


RUN mkdir /var/run/nginx
RUN mkdir /var/run/zabbix; chown zabbix /var/run/zabbix
RUN mkdir /run/php

COPY copy/etc/supervisor/conf.d/zabbix.conf /etc/supervisor/conf.d
COPY copy/sbin/prepare_magic.sh /sbin
RUN chmod a+x /sbin/prepare_magic.sh

COPY copy/usr/local/etc/zabbix_server.conf /usr/local/etc/zabbix
COPY copy/usr/local/web/zabbix/conf/zabbix.conf.php /usr/local/web/zabbix/conf
COPY copy/etc/php/7.0/fpm/php.ini /etc/php/7.0/fpm
COPY copy/etc/nginx/nginx.conf etc/nginx
COPY copy/etc/nginx/cert.pem etc/nginx
COPY copy/etc/nginx/cert.key etc/nginx

VOLUME ["/var/log"]

EXPOSE 443
