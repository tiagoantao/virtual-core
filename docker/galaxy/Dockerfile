FROM quay.io/bgruening/galaxy:16.10
MAINTAINER Tiago Antao <tiagoantao@gmail.com>


RUN apt-get update -y

RUN apt-get install -y openssh-server proftpd-mod-ldap libldap2-dev libsasl2-dev
RUN ssh-keygen -A
RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh
COPY copy/etc/supervisor/conf.d/sshd.conf /etc/supervisor/conf.d

COPY copy/etc/nginx/cert.key /etc/nginx
COPY copy/etc/nginx/cert.pem /etc/nginx
COPY copy/etc/nginx/nginx.conf /etc/nginx


COPY copy/etc/galaxy/reports_wsgi.ini /etc/galaxy
COPY copy/galaxy-central/config/auth_conf.xml /galaxy-central/config
COPY copy/etc/galaxy/galaxy.ini /etc/galaxy

COPY copy/etc/proftpd/modules.conf /etc/proftpd
COPY copy/etc/proftpd/proftpd.conf /etc/proftpd


ENV NONUSE postgres
COPY copy/usr/local/bin/check_database.py /usr/local/bin
RUN chmod a+x /usr/local/bin/check_database.py


EXPOSE 9002 8800 2222 443 80 21
