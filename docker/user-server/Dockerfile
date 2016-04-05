FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

COPY ldap.conf /etc/
COPY authorized_keys /root/.ssh
COPY skel-profile /etc/skel/.profile

RUN mkdir /core
RUN mkdir /core/software

VOLUME ["/core/software", "/home"]

COPY add_software.sh /
RUN bash /add_software.sh
RUN rm /add_software.sh
