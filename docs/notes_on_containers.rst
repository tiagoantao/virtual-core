Notes on containers
*******************

------------------
Support containers
------------------

These are available in dockerhub. There are two different flavors: Alpine
and Ubuntu-based.

All Virtual Core containers are based on either
alpine-supervisor-sshd or tiagoantao/ubuntu-supervisor-sshd.
These have the following features:

#. Processes are controlled by supervisord
#. Includes a zabbix monitor
#. A SSH deamon is installed
   * A authorized_key has to be supplied. Used for root access.
#. The entry point is `/sbin/server_run.sh`. A file `/sbin/prepare_magic.sh`
   can be installed and will be called before supervisor (e.g. to use
   passed environment variables to setup stuff) 

.. TODO::
   Discuss shared volumes and the need of consistent mount points

.. TODO::
   Talk about docker swarm


------------
LDAP service
------------

Both containers are based on Alpine Linux. This will probably change in
the future as Alpine Linux is not a good solution for most other services.


ldap
----

.. attention::
   The container exposes only the SSL port, but a non-SSL port is available
   inside the docker network.

--------------------------------
PostgreSQL service and container
--------------------------------

The PostgreSQL database is configured by default to authenticate via
LDAP, but some databases are trusted to other hosts, these are normally
related to other containers. For example the zabbix database is
controlled by the user zabbix which is trusted to login from the host
zabbix. Note a few things:

#. This is a default behavior that you can change during the
   configuration stage
#. All databases necessary by other containers are created along with
   access rights **even for containers that are not going to be installed**.
   Note that the database schemas should be created by the respective
   containers.
#. Make sure you are happy with access rules, especially if you spread
   containers across multiple machines. In that case you have some
   tweaking to do.


-----------
Web service
-----------

uwsgi - same directory as static, extension cgi

traverse...

discuss architecture


-----------
File router
-----------

The samba user is not LDAP based. Password supplied in the clear

------------------
Software container
------------------


-------------
Compute nodes
-------------

We provide support for clusters via SLURM_. You can be in one of three situations:

#. You already have a cluster infrastructure not based on SLURM. If that is your
case we do not support this directly. But if your cluster is based on free software
we would be most happy to try to support it, please do contact us!
#. You already have a SLURM based configuration. In this case you will have to
make a few changes to the configuration. The wizard will help you here.
#. You have nothing installed. We will take care of setting up a complete SLURM
solution.


-----------
User server
-----------

based on software container.
It is also a SLURM head node (if desired).

-----------------------------------------
Exploratory analysis (Jupyter Lab) server
-----------------------------------------

based on user server

share the home dirs...

.. _SLURM: http://slurm.schedmd.com/slurm.html
