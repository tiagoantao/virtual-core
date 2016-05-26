=============================================
LDAP authentication based on the virtual core
=============================================


Here we present an example with Ubuntu, hopefully the added comments
are enough to help with other operating systems.


`apt-get install libpam-ldap ldap-utls`


ldap-utils is recommended, not required.

On the configuration you will need to supply your LDAP URL (with https)
and your base DN. You probably will want to allow users to change their
passwords (with impact on the LDAP server). The server is not authenticated.

This will change the PAM configuration on /etc/pam.d. It will also
change /etc/ldap.conf

If you are using your own certificate authority, you will need to add
the certificate of the authority, by changing the `TLS_CACERT` parameter
on /etc/ldap/ldap.conf . Be careful with auto-reconfiguration

Finally do

`pam-auth-update`


And you should be done

https://wiki.debian.org/LDAP/PAM



(uid limitation - pam_filter)
