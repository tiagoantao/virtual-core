#############################
Virtual core for data science
#############################

Virtual Core is a turn-key solution to deploy a complete set of data-science
core services that can be used as a base infrastructure for big data analysis.
It was developed to support bioinformatics data analysis at the University of
Montana.

The solution is based on Docker_  and it currently includes:

- A LDAP container, along with a web interface (phpldapadmin)

- Zabbix-based monitoring.

- PostgreSQL database server.

- An extensible software container, currently including Python and R tools for data-science (based on Anaconda)

- A user container, where users can log-in and run all data-science applications

- A file server, capable of routing data from other file servers (e.g. communicate with a Samba server and exposing an NFS interface)

- Cluster software (currently only SLURM)

- A SLURM-compute container that can be deployed across a cluster (via Docker swarm)

- A exploratory analysis server, which includes a `Jupyter hub`_

- Plain web server

Most communications are SSL secured and the system can work as a adhoc
SSL certification authority.

The containers can be split across a cluster with Docker Swarm.

A wizard is included to get a single-machine configuration up and running.

The system can be extended with flavors (Natural Language Processing, Finance,
costumer analysis).

We currently have a flavor for bioinformatics with a
Galaxy container, extra analysis software (based on bioconda) and the file router
can be configured to receive data from Illumina Sequencers.

.. warning::
    Virtual Core is currently in production an the University of Montana, but
    its installation by others is still quite hard. We are working hard to
    produce documentation, but that is still under heavy development (as you
    can see here). Some functionality is still being finalized.
    That being said, you are most welcome to try this (pre-alpha quality)
    software. If you need any help, do not hesitate to contact me_.

Contents
========

.. toctree::

    install
    notes_on_containers
    file_router
    customizing_system
    ldap_on_servers
    bioinformatics

.. _Docker: https://docker.com
.. _`Jupyter hub`: http://jupyter.org/
.. _me: mailto:tiagoantao@gmail.com
