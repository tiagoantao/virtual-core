FROM tiagoantao/alpine-base
ARG BASE=dc=example,dc=com
ARG URI=ldap://ldap.example.com
ARG PASS=obvious
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb

VOLUME /var/lib/openldap/openldap-data

EXPOSE 389
RUN echo BASE $BASE >> /etc/openldap.conf && echo URI $URI >> /etc/openldap.conf
RUN 
