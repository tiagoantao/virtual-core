Installation
************

Here you can find a set of containers to help creating a data science core architecture, for example:

- LDAP server
- PostgreSQL server
- File router (NFS and Samba)
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


Virtual Core **uses Docker swarm mode.** You can check the `Swarm mode`_
documentation, though we provide basic instructions::

    docker swarm init

Virtual core requires a **local Docker registry**. Again you can find
`documentation on the Docker site`_, but you probably only need to do this::

    docker run -d -p 5000:5000 --name registry registry:2

.. TODO:
    This is wrong, one needs a certificate



This will install all your servers on the local machine. If you have a very
large big-iron machine, this might be what you want. If you have a cluster,
this is still a reasonable starting point, though you will have some work to
do, especially on the security front.

#. Make sure you have a docker with swarm mode installation running.
#. Use the wizard to configure the most complicated stuff: ``./run_wizard.sh``
#. Create an overlay virtual network called `virtual_core` ``docker network
create --driver overlay --subnet 172.18.0.0/24 virtual_core``. **Make sure this
is configured everytime you start the system**. **Also make sure the subnet is
OK for you**.
#. Create a directory that will store all your docker volumes. This might need
to be very big. Lets call this your base directory.
#. ``cp etc/hosts.sample etc/hosts`` (you will want to edit this in the future)
#. Make sure all variables on ``ansible/`` are correctly defined, especially on
the common role
#. ``python src/create_directory_structure.py <base_directory>``
#. ``cd _instance/ansible; ansible-playbook --ask-pass -i ../../etc/hosts main.yml``


Installation on a cluster
-------------------------

Swarm node joining

The registry shoud be on the head node.

CONTINUE

.. _`Swarm mode`: https://docs.docker.com/engine/swarm/
.. _`documentation on the Docker site`: https://docs.docker.com/registry/
