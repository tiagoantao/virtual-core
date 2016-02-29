------------------------------------------------
A Bioinformatics core based on Docker containers
------------------------------------------------

Here you can find a set of containers to help creating a bioinformatics core architecture, for example:

- LDAP server
- PostgreSQL server
- NFS server
- Galaxy server
- Zabbix server
- Software server (i.e. a lot of pre-installed software)
- Interative Compute server (a place for users to login)
- SLURM head node
- SLURM node

Base images
-----------

We use Alpine Linux for simple servers (very small footprint)
and Ubuntu for larger images. It might happen that some containers
are derived from Debian ones.


Todo: script to create docker volume directory structure

Dependencies
------------

- Python 3
- PyYAML
- Docker
- Ansible (including playbook)


Installation
------------

1. Create a directory that will store all your docker volumes. This might need to be
very big
2. Do ``python3 src/copy_templates.py [Directory_Above]``
