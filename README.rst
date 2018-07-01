------------------------------------------------
A Data Science core based on Docker containers
------------------------------------------------

Warning
-------

virtual-core has been superseded by Skates_


Summary
-------

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

Installation
------------

Please check the `project documentation`_.

Acknowledgements
----------------

The sequencer Samba file configuration was originally inspired on David Personette's `Samba container`_.
It is currently completely different.

The current Galaxy configuration is based on Björn Grüning's `Galaxy container`_.


Author and License
------------------

Copyright by Tiago Antao. Licensed under GNU Affero General Public License
version 3.


.. _project documentation: http://virtual-core.rtfd.io/
.. _Galaxy container: https://github.com/bgruening/docker-galaxy-stable
.. _Samba container: https://github.com/dperson/samba
.. _Skates: https://gitlab.com/tiagoantao/skates
