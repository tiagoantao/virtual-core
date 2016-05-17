FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add php-fpm nginx
RUN apk add phpldapadmin php-openssl php-gettext php-xml php-ldap

COPY copy/etc/supervisor.d/phpldap.ini /etc/supervisor.d
COPY authorized_keys /root/.ssh

VOLUME ["/var/log", "/etc/php", "/etc/phpadmin", "/etc/nginx"]
#Do we need /etc/php and /etc/phpadmin as a Export?

EXPOSE 443

