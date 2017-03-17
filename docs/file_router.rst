The file router container
*************************

The file router container serves two purposes:

* Export NFS volumes
* Interacting with Windows machines

------------------
Export NFS volumes
------------------

To export NFS volumes, configure the NFS exports file appropriately (see an example on copy/etc/exports.sample

---------------------------------
Interacting with Windows machines
---------------------------------

There are a few use cases here:

* Interacting with services that are on Windows (For example, Illumina sequencers)
* Exporting volumes to users

.. warning::
    Integration of LDAP and Windows authentication is nothing short of a mess.
    There are plenty of alternatives on how to do it, but unless you *really* have to do it, you might want to
    consider avoiding it. There is plenty of documentation on the web, and we will not
    
If you want users to be able to mount your volumes as samba shares and have integrated LDAP authentication,
we offer a ad-hoc script `/usr/bin/change_password.py` that does sync between samba and LDAP. It works this way:

1. The user already has an account on LDAP
2. You create an account for the user on Samba using ``pdbedit -a ldap_uid``. Use ``smbpasswd ldap_uid``, password will be ``boot``
3. The user logs in, ASAP, on the file_router and uses ``change_password.py boot`` to sync the passwords
4. From now on the user can login on the file_router to change the password using ``change_password.py``
  (indeed password change can only happen on the file_router or the passwords will be out of sync)

Yes, this is ugly, but LDAP/Samba/Windows AD integration is ugly.

Note that for ad-hoc users (for example, in the bioinformatics case, interacting with a Illumina sequencer)
you can just mantain a separate account just on samba without LDAP sync.
