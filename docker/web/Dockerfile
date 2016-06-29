FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y nginx php php-fpm php-ldap

RUN mkdir /run/php
COPY authorized_keys /root/.ssh
#COPY copy/etc/nginx/cert.key /etc/nginx
#COPY copy/etc/nginx/cert.pem /etc/nginx
#COPY copy/etc/nginx/nginx.conf /etc/nginx

VOLUME ["/var/log", "/var/www/"]

EXPOSE 80
