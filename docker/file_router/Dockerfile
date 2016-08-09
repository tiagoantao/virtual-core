FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y nfs-kernel-server samba


COPY authorized_keys /root/.ssh 

#samba
COPY copy/etc/samba/smb.conf /etc/samba
COPY copy/etc/samba/users /etc/samba
COPY copy/etc/supervisor/conf.d/samba.conf /etc/supervisor/conf.d

#NFS
#COPY exports /etc/exports
#COPY run.sh run.sh

COPY copy/sbin/prepare_magic.sh /sbin

RUN mkdir /vcore

#EXPOSE 111/tcp 111/udp 2049 137 139 445
EXPOSE 137 139 445

VOLUME ["/var/log"]
