FROM tiagoantao/ubuntu-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apt-get update
RUN apt-get install -yy postgresql postgresql-client libpq-dev sudo

#Making sure we are on version 9.5
RUN ver=`pg_config --version`; if [ "${ver#*$9.5}" = "$ver" ]; then exit 1; fi

COPY copy/etc/supervisor.d/postgres.conf /etc/supervisor/conf.d

#We will initiate the data dir only if it is empty, so we copy to a temporary one
RUN rm -rf /var/lib/postgresql/*
RUN mkdir -p /copy/var/lib/postgresql/data
COPY copy/sbin/prepare_magic.sh /sbin
COPY copy/var/lib/postgresql/data/pg_hba.conf /copy/var/lib/postgresql/data
COPY copy/var/lib/postgresql/data/postgresql.conf /copy/var/lib/postgresql/data

COPY copy/var/lib/postgresql/data/server.crt /copy/var/lib/postgresql/data
COPY copy/var/lib/postgresql/data/server.key /copy/var/lib/postgresql/data
RUN chmod 0600 /copy/var/lib/postgresql/data/server.key
RUN chown postgres.postgres /copy/var/lib/postgresql/data/*
RUN locale-gen en_US.utf8

COPY authorized_keys /root/.ssh

VOLUME ["/var/lib/postgresql"]

EXPOSE 5432
