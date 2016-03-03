------------------------------------------------
A Bioinformatics core based on Docker containers
------------------------------------------------

Here you can find a set of containers to help creating a bioinformatics core architecture, for example:

- LDAP server
- PostgreSQL server
- NFS server (Not active)
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

- Python 3.5+
- PyYAML
- Docker
- Ansible (including playbook)


Installation
------------

This will install all your servers on the local machine. If you have a very large
big-iron machine, this might be what you want. If you have a cluster, this is still
a reasonable starting point.

1. Create a directory that will store all your docker volumes. This might need to be
very big.

2. ``python3 src/prepare_templates.py [Directory_Above]`` . Prepares the ansible
templates (this probably can be put inside ansible). 

3. ``python3 src/use_examples.py`` . This will copy the example configuration files
to be used as the default ones. Make sure to change things in your final configuaration.

4. ``python3 src/create_directory_structure.py [Directory_Above]``


4. ``cp ansible/etc/host.sample ansible/etc/hosts``

5. ``cd ansible; ansible-playbook --ask-pass -i etc/hosts main.yml```
