FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y nfs-common

COPY copy/etc/ldap.conf /etc/
COPY authorized_keys /root/.ssh
COPY copy/etc/skel/.profile /etc/skel/.profile

RUN mkdir /data

RUN mkdir /core
RUN mkdir /core/software

VOLUME ["/core/software", "/home"]

COPY add_software.sh /
RUN bash /add_software.sh
RUN rm /add_software.sh
