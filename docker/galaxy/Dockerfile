FROM quay.io/bgruening/galaxy:16.04
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y libsasl2-dev libldap2-dev proftpd-mod-ldap
RUN apt-get install -y openssh-server

COPY copy/etc/galaxy.ini /etc/galaxy
COPY copy/etc/galaxy/reports_wsgi.ini /etc/galaxy
COPY copy/galaxy-central/config/auth_conf.xml /galaxy-central/config
COPY copy/etc/supervisor/conf.d/galaxy.conf /etc/supervisor/conf.d
COPY copy/etc/proftpd/modules.conf /etc/proftpd
COPY copy/etc/proftpd/proftpd.conf /etc/proftpd

RUN ssh-keygen -A
RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh

#Bug on image, correcting:
COPY /copy/add_ldap.sh /
RUN bash /add_ldap.sh; rm /add_ldap.sh

