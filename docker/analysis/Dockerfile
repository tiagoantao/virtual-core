FROM core_analysis
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y npm
RUN npm install -g configurable-http-proxy

COPY authorized_keys /root/.ssh

RUN mkdir -p /etc/jupyterhub
RUN mkdir -p /srv/jupyterhub

COPY copy/etc/jupyterhub/jupyterhub_config.py /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.pem /etc/jupyterhub
COPY copy/etc/jupyterhub/cert.key /etc/jupyterhub
COPY copy/etc/supervisor/conf.d/jupyterhub.conf /etc/supervisor/conf.d

RUN openssl rand -base64 2048 > /srv/jupyterhub/cookie_secret
RUN chmod 0600 /srv/jupyterhub/cookie_secret
RUN openssl rand -hex 32 > /srv/jupyterhub/proxy_secret

VOLUME ["/vcore/software", "/home", "/var/log/"]
RUN rm /core; ln -s /vcore /core  # legacy

EXPOSE :443
