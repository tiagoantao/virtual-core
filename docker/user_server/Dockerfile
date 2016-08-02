FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update -y
RUN apt-get install -y nfs-common
RUN apt-get install -y slurm-client

COPY authorized_keys /root/.ssh

COPY copy/etc/ldap.conf /etc/
COPY copy/etc/skel/.profile /etc/skel/.profile
COPY copy/etc/pam.d/* /etc/pam.d/
COPY copy/etc/nsswitch.conf /etc/

#munge, for slurm
COPY munge.key /etc/munge
RUN chown munge.munge /etc/munge/munge.key
RUN chmod 0400 /etc/munge/munge.key
RUN mkdir /var/run/munge
RUN chown munge.munge /var/run/munge
RUN chown munge.munge /var/log/munge
COPY copy/etc/supervisor/conf.d/munge.conf /etc/supervisor/conf.d
COPY copy/etc/slurm-llnl/slurm.conf /etc/slurm-llnl

RUN mkdir -p /vcore/software
RUN mkdir /scratch

VOLUME ["/vcore/software", "/home", "/var/log/", "/scratch"]

COPY /copy/sbin/add_software.sh /sbin
RUN bash /sbin/add_software.sh
