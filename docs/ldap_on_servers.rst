LDAP authentication based on the virtual core
=============================================

Example: ubuntu server
apt-get install libpam-ldap

recommend installing ldap-utils (e.g. testing with ldapsearch)




/etc/ldap.conf (dpkg-reconfigure?)
uri with ldaps
pam_password exop ?
TLS_CACERT /etc/ssl/ca.cert (gnutls caveat)

/etc/ldap/ldap.conf
TLS_CACERT

https://wiki.debian.org/LDAP/PAM

pam-auth-update


(uid limitation - pam_filter)
