#!/usr/bin./python
import getpass
import sys

import pexpect


boot = False
if len(sys.argv) > 1 and sys.argv[1] == 'boot':
    print "Boot mode"
    boot = True


def get_passes():
    old = getpass.getpass('Old password: ')
    new1 = 'a'
    new2 = 'b'
    while new1 != new2:
        new1 = getpass.getpass('New password: ')
        new2 = getpass.getpass('New password (repeat): ')
    return old, new1


def change_password(old=None, new=None):
    if old is None:
        old, new = get_passes()
    p = pexpect.spawn('passwd')
    p.expect('password')
    p.sendline(old + '\n')
    outcome = p.expect(['New', 'incorrect', 'error'])
    p.sendline(new + '\n')
    try:
        outcome = p.expect('new password:', timeout=1)
        if p.match is None:
            print p.buffer, 'new password'
        else:
            p.sendline(new + '\n')
            outcome = p.expect(['success'] , timeout=1)
            if p.match is not None:
                return old, new
    except:
        print p.buffer, 'top level'
    return False


def change_samba_password(old, new)
    p = pexpect.spawn('smbpasswd')
    p.expect('Old SMB password:')
    p.sendline(old + '\n')
    p.expect('New SMB password:')
    p.sendline(new + '\n')
    p.expect('Retype new SMB password:')
    p.sendline(new + '\n')
    p.expect('Password changed', timeout=2)
    if p.match is None:
        return False
    else:
        return True

pwds = change_password()
while not pwds:
    pwds = change_password()
old, new = pwds
if not change_samba_password('boot' if boot else old, new):
    print 'Samba password change failed, reverting ldap password'
    change_password(new, old)
