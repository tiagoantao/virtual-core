Installation
************

Here you can find a set of containers to help creating a data science core architecture, for example:

- LDAP server
- PostgreSQL server
- NFS server (Not active)
- Samba server (for integration with sequencer technology like Illumina)
- Galaxy server
- Zabbix server
- Software server (i.e. a lot of pre-installed software)
- Interative Compute server (a place for users to login)
- Exploratory Analysis server (JupyterHub with JupyterLab)
- SLURM grid configuration

There is a focus on bioinformatics, but the infrastructure can be used for
other applications.

Base images
-----------

We use Alpine Linux for simple servers (very small footprint)
and Ubuntu for larger images. It might happen that some containers
are derived from Debian ones.


Dependencies
------------

- Python 2.7 (for ansible) **and** 3.5+
- PyYAML
- Docker
- Ansible
- docker-py (python-docker on ubuntu)

.. TODO::
    Check Python version for ansible (conda...)

**If you use the setup wizard** (strongly recommended for a first install)

- Flask
- openssl and pyOpenSSL (if you need to generate keys)

(explain with conda)


Installation
------------


This will install all your servers on the local machine. If you have a very large
big-iron machine, this might be what you want. If you have a cluster, this is still
a reasonable starting point, though you will have some work to do, especially
on the security front.

#. Use the wizard to configure the most complicated stuff: ``./run_wizard.sh``
#. Create a virtual network called `virtual_core` ``docker network create virtual_core``. **Make sure this is configured everytime you start the system**
#. Create a directory that will store all your docker volumes. This might need to be very big.
#. ``cp etc/hosts.sample etc/hosts`` (you will want to edit this in the future)
#. ``cd _instance/ansible; ansible-playbook --ask-pass -i ../../etc/hosts main.yml``

Acknowledgements
----------------

The sequencer Samba file configuration was originally inspired on David Personette's `Samba container`_.
It is currently completely different.

The current Galaxy configuration is based on Björn Grüning's `Galaxy container`_.


Author and License
------------------

Copyright by Tiago Antao. Licensed under GNU Affero General Public License
version 3.


.. _the most recent version: http://docs.ansible.com/ansible/intro_installation.html
.. _Galaxy container: https://github.com/bgruening/docker-galaxy-stable
.. _Samba container: https://github.com/dperson/samba
