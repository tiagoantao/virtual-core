FROM postgres:9.5
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

#RUN apk add postgresql postgresql-client
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get install -y openssh-server
RUN ssh-keygen -A
RUN echo root:bla | chpasswd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN echo PasswordAuthentication yes >> /etc/ssh/sshd_config

COPY run.sh /run.sh
COPY supervisord.conf /etc/supervisord.conf

VOLUME ["/var/lib/postgresql"]

EXPOSE 5432

CMD ["bash", "run.sh"]
