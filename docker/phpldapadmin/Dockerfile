FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y nginx php php-fpm php-ldap
RUN apt-get install -y  phpldapadmin

RUN mkdir /run/php
COPY copy/etc/supervisor/conf.d/phpldap.conf /etc/supervisor/conf.d
COPY authorized_keys /root/.ssh
COPY copy/etc/nginx/cert.key /etc/nginx
COPY copy/etc/nginx/cert.pem /etc/nginx
COPY copy/etc/nginx/nginx.conf /etc/nginx
COPY copy/etc/phpldapadmin/config.php /etc/phpldapadmin

VOLUME ["/var/log"]

EXPOSE 443

