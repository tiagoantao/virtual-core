FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb

COPY supervisord.conf /etc/supervisord.conf

VOLUME ["/var/log/", "/var/lib/openldap/", "/var/run/openldap/", "/etc/openldap"]

EXPOSE 389

CMD ["supervisord"]
