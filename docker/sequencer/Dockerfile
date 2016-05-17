FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add samba

COPY authorized_keys /root/.ssh

COPY copy/usr/sbin/samba.sh /usr/sbin/samba.sh
COPY copy/etc/samba/smb.conf /etc/samba
COPY copy/etc/samba/gdbcommands /etc/samba
COPY copy/etc/supervisor.d/samba.ini /etc/supervisor.d

RUN chmod a+x /usr/sbin/samba.sh

RUN mkdir /sequencer

VOLUME ["/sequencer"]

EXPOSE 137 139 445
