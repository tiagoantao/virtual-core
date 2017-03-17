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
    p.sendline(new1 + '\n')
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

pwds = change_password()
while pwds == False:
    pwds = change_password()
old, new = pwds
