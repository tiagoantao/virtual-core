FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -y slurm-wlm

#RUN mkdir /run/php
COPY authorized_keys /root/.ssh

COPY munge.key /etc/munge
RUN chown munge.munge /etc/munge/munge.key
RUN chmod 0400 /etc/munge/munge.key
RUN mkdir /var/run/munge
RUN chown munge.munge /var/run/munge
RUN chown munge.munge /var/log/munge

COPY copy/etc/slurm-llnl/slurm.conf /etc/slurm-llnl
COPY copy/etc/supervisor/conf.d/slurm.conf /etc/supervisor/conf.d/

VOLUME ["/var/log", "/var/spool/"]

EXPOSE 10389 6817 6818
