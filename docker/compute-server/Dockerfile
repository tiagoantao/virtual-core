FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y slurm-wlm

#RUN mkdir /run/php
COPY authorized_keys /root/.ssh

RUN create-munge-key

VOLUME ["/var/log", "/var/spool/"]

EXPOSE 10389 6817 6818
