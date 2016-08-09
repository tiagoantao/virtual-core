FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y nfs-kernel-server samba
RUN apt-get install -y nginx uwsgi-plugin-python3 python3-pip
RUN apt-get install -y python3-flask python3-flask python3-flask python3-ldap3
RUN pip3 install flask-login


COPY authorized_keys /root/.ssh 

#samba
COPY copy/etc/samba/smb.conf /etc/samba
COPY copy/etc/samba/users /etc/samba
COPY copy/etc/supervisor/conf.d/samba.conf /etc/supervisor/conf.d

#NFS
#COPY exports /etc/exports
#COPY run.sh run.sh


#nginx
RUN mkdir /var/run/nginx
COPY copy/etc/nginx/nginx.conf /etc/nginx
COPY copy/etc/nginx/cert.pem /etc/nginx
COPY copy/etc/nginx/cert.key /etc/nginx

COPY copy/sbin/prepare_magic.sh /sbin

#sequencer-router
COPY copy/etc/sequencer-router.conf /etc
COPY sequencer-router sequencer-router
COPY copy/etc/supervisor/conf.d/sequencer-router.conf /etc/supervisor/conf.d

RUN mkdir /vcore

#EXPOSE 111/tcp 111/udp 2049 137 139 445 443
EXPOSE 137 139 445 443

VOLUME ["/var/log"]
