FROM ubuntu
#FROM tiagoantao/alpine-base
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

#RUN apk add nfs-utils
#RUN apk add openssh
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y nfs-kernel-server supervisor
RUN apt-get install -y openssh-server
RUN ssh-keygen -A
RUN echo root:bla | chpasswd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN echo PasswordAuthentication yes >> /etc/ssh/sshd_config

COPY supervisord.conf /etc/supervisord.conf

COPY exports /etc/exports
COPY run.sh run.sh

RUN mkdir /core

EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp

CMD ["/bin/bash", "run.sh"]
