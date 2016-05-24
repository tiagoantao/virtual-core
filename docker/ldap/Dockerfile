FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add openldap openldap-back-bdb openldap-clients

COPY copy/etc/supervisor.d/ldap.ini /etc/supervisor.d

COPY authorized_keys /root/.ssh
RUN chmod 0600 /root/.ssh/authorized_keys

VOLUME ["/etc/openldap", "/var/log/", "/var/lib/openldap/", "/var/run/openldap/"]

EXPOSE 636
