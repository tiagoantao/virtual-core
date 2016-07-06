FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y php php-fpm php-ldap
RUN apt-get install -y nginx uwsgi-plugin-ldap uwsgi-plugin-python3

#RUN mkdir /run/php
COPY authorized_keys /root/.ssh
COPY copy/etc/supervisor/conf.d/nginx.conf /etc/supervisor/conf.d
RUN mkdir /etc/uwsgi
COPY copy/etc/uwsgi/uwsgi.ini /etc/uwsgi

#COPY copy/etc/nginx/cert.key /etc/nginx
#COPY copy/etc/nginx/cert.pem /etc/nginx
#COPY copy/etc/nginx/nginx.conf /etc/nginx
#COPY copy/etc/nginx/conf.d/default /etc/nginx

VOLUME ["/var/log", "/var/www/"]

EXPOSE 80
