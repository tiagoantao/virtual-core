FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add php-fpm nginx openssh
RUN apk add php-fpm phpldapadmin php-openssl php-gettext php-xml php-ldap
RUN ssh-keygen -A
RUN echo root:bla | chpasswd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN echo PasswordAuthentication yes >> /etc/ssh/sshd_config

COPY supervisord.conf /etc/supervisord.conf

VOLUME ["/var/log", "/etc/php", "/etc/phpadmin", "/etc/nginx"]

EXPOSE 8389

CMD ["supervisord"]
