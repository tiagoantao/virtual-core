FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb

COPY etc/openldap/slapd.conf /etc/openldap
COPY etc/openldap/ldap.conf /etc/openldap
COPY etc/openldap/DB_CONFIG /etc/openldap

VOLUME ["/var/lib/openldap/openldap-data", "/var/run/openldap/", "/etc/openldap"]

EXPOSE 389
