FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk add openldap openldap-back-bdb openldap-clients
RUN apk add openssh
RUN ssh-keygen -A
RUN echo root:bla | chpasswd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN echo PasswordAuthentication yes >> /etc/ssh/sshd_config

COPY supervisord.conf /etc/supervisord.conf

VOLUME ["/var/log/", "/var/lib/openldap/", "/var/run/openldap/", "/etc/openldap"]

EXPOSE 389

CMD ["supervisord"]
