FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb openldap-clients

COPY etc/supervisor.d/ldap.ini /etc/supervisor.d

VOLUME ["/var/log/", "/var/lib/openldap/", "/var/run/openldap/"]

EXPOSE 389
