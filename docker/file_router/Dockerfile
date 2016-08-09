FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y nfs-kernel-server
RUN apt-get install -y samba


COPY authorized_keys /root/.ssh 

#samba
COPY copy/etc/samba/smb.conf /etc/samba

#NFS
#COPY exports /etc/exports
#COPY run.sh run.sh

RUN mkdir /vcore

#EXPOSE 111/tcp 111/udp 2049 137 139 445
EXPOSE 137 139 445

VOLUME ["/var/log"]
