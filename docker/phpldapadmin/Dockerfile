FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add php-fpm phpldapadmin nginx

VOLUME ["/var/log", "/etc/php", "/etc/phpadmin", "/etc/nginx"]

EXPOSE 8369

CMD ["/usr/sbin/nginx"]
