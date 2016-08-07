FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

COPY authorized_keys /root/.ssh

RUN mkdir -p /vcore/software
RUN mkdir /software_utils

VOLUME ["/vcore/software"]
