FROM core_user_server
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y

COPY authorized_keys /root/.ssh

COPY copy/etc/jupyterhub/jupyterhub_config.py /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.pem /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.key /etc/jupyterhub

VOLUME ["/vcore/software", "/home", "/var/log/", "/scratch"]

EXPOSE :80
EXPOSE :443
