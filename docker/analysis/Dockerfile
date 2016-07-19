FROM core_user_server
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

#RUN apt-get update -y

COPY authorized_keys /root/.ssh

RUN mkdir -p /etc/jupyterhub
RUN mkdir -p /srv/jupyterhub

COPY copy/etc/jupyterhub/jupyterhub_config.py /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.pem /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.key /etc/jupyterhub

RUN openssl rand -base64 2048 > /srv/jupyterhub/cookie_secret
RUN openssl rand -hex 32 > /src/jupterhub/proxy_secret

VOLUME ["/vcore/software", "/home", "/var/log/"]

EXPOSE :443
