===================
Notes on containers
===================

------------------
Support containers
------------------

These are available in dockerhub. There are two different flavors: Alpine
and Ubuntu-based.

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
