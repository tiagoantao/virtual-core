FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y nfs-common

COPY authorized_keys /root/.ssh

COPY copy/etc/ldap.conf /etc/
COPY copy/etc/skel/.profile /etc/skel/.profile
COPY copy/etc/pam.d/* /etc/pam.d/
COPY copy/etc/nsswitch.conf /etc/

RUN mkdir /core
RUN mkdir /core/software
RUN mkdir /scratch

VOLUME ["/core/software", "/home", "/var/log/", "/scratch"]

COPY /copy/sbin/add_software.sh /sbin
RUN bash /sbin/add_software.sh
