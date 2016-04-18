FROM ubuntu:15.10
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y supervisor libpam-ldap bash
RUN apt-get install -y openssh-server
RUN apt-get install -y python3 wget

#this machine cannot be run without adding a root key
#(and server key should be changed also)

#You probably also need a /etc/ldap.conf

#Explain prepare magic somewhere

#Install Linking of configuration files and entrypoint
RUN wget --no-check-certificate  https://raw.githubusercontent.com/tiagoantao/mutable_files/master/link_mutable_files.py -O /sbin/link_mutable_files.py
COPY copy/sbin/server_run.sh /sbin
RUN chmod a+x /sbin/server_run.sh /sbin/link_mutable_files.py
RUN mkdir /traverse

COPY copy/etc/supervisor/conf.d/supervisor.conf /etc/supervisor/conf.d/
COPY copy/etc/supervisor/conf.d/supervisor-sshd.conf /etc/supervisor/conf.d/

RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh

#EXPOSE 22

CMD ["/sbin/server_run.sh"]
