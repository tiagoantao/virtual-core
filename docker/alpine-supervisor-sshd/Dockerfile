FROM tiagoantao/alpine-base
MAINTAINER  Tiago Antao <tiagoantao@gmail.com>

RUN apk upgrade
RUN apk add supervisor nss-pam-ldapd
RUN apk add openssh bash

#this machine cannot be run without adding a root key
#(and server key should be changed also)

COPY sbin/server_run.sh /sbin
RUN chmod a+x /sbin/server_run.sh

COPY etc/supervisor.d/supervisor.ini /etc/supervisor.d/
COPY etc/supervisor.d/supervisor-sshd.ini /etc/supervisor.d/

COPY etc/ssh/sshd_config /etc/ssh/
RUN ssh-keygen -A
RUN mkdir /root/.ssh

EXPOSE 22

CMD ["/sbin/server_run.sh"]
