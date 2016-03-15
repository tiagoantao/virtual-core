FROM ubuntu:15.10
MAINTAINER  Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y supervisor libpam-ldap
RUN apt-get install -y openssh-server

#this machine cannot be run without adding a root key
#(and server key should be changed also)

#You probably also need a /etc/ldap.conf

COPY supervisor.conf /etc/supervisor/conf.d/
COPY supervisor-sshd.conf /etc/supervisor/conf.d/

RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh

EXPOSE 22

CMD ["/usr/bin/supervisord"]
