#!/usr/bin./python
import getpass
import pexpect

def change_password():
    old = getpass.getpass('Old password: ')
    new1 = 'a'
    new2 = 'b'
    while new1 != new2:
        new1 = getpass.getpass('New password: ')
        new2 = getpass.getpass('New password (repeat): ')
    p = pexpect.spawn('passwd')
    p.expect('password')
    p.sendline(old + '\n')
    outcome = p.expect(['New', 'incorrect', 'error'])
    p.sendline(new1 + '\n')
    try:
        outcome = p.expect('new password:', timeout=1)
        if p.match is None:
            print p.buffer, 555599999
        else:
            p.sendline(new1 + '\n')
            outcome = p.expect(['success'] , timeout=1)
            if p.match is not None:
                return new1
    except:
        print p.buffer, p
    return False

pwd = change_password()
while pwd == False:
    pwd = change_password()

