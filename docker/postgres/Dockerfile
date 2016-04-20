FROM tiagoantao/alpine-supervisor-sshd
MAINTAINER Tiago Antao <tiagoantao@gmail.com>

RUN apk update
RUN apk add postgresql postgresql-client sudo

#Making sure we are on version 9.5
RUN ver=`pg_config --version`; if [ ${ver:10:4} != "9.5" ]; then exit 1; fi

COPY copy/etc/supervisor.d/postgres.ini /etc/supervisor.d

#We will initiate the data dir only if it is empty, so we copy to a temporary one
COPY copy/sbin/prepare_magic.sh /sbin
RUN mkdir -p /copy/var/lib/postgresql/data
COPY copy/var/lib/postgresql/data/pg_hba.conf /copy/var/lib/postgresql/data
COPY copy/var/lib/postgresql/data/postgresql.conf /copy/var/lib/postgresql/data

COPY copy/var/lib/postgresql/data/server.crt /copy/var/lib/postgresql/data
COPY copy/var/lib/postgresql/data/server.key /copy/var/lib/postgresql/data
RUN chown postgres.postgres /copy/var/lib/postgresql/data/*

COPY authorized_keys /root/.ssh

VOLUME ["/var/lib/postgresql"]

EXPOSE 5432
