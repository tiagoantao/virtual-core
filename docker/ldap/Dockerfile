FROM tiagoantao/alpine-base
ARG BASE=dc=example,dc=com
ARG URI=ldap://ldap.example.com
ARG PASS=obvious
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb

RUN cp /etc/openldap/DB_CONFIG.example /etc/openldap/DB_CONFIG 

VOLUME /var/lib/openldap/openldap-data

EXPOSE 389
