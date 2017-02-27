import os
import shutil


def create_ca(my_dir='etc/ca', ca_name='demoCA'):
    complete_dir = my_dir + os.sep + ca_name
    if os.path.exists(complete_dir):
        return
    os.mkdir(complete_dir)
    os.mkdir(complete_dir + '/certs')
    os.mkdir(complete_dir + '/crl')
    os.mkdir(complete_dir + '/newcerts')
    os.mkdir(complete_dir + '/private')
    w = open(complete_dir + '/index.txt', 'w')
    w.close()
    ret = os.system('openssl req -new -keyout {complete_dir}/private/cakey.pem -config init.ssl -nodes -out {complete_dir}/careq.pem'.format(complete_dir=complete_dir))
    # 2000 is number of days (arbitrary, really)
    if ret != 0:
        return False
    cwd = os.getcwd()
    os.chdir(my_dir)
    ret = os.system('openssl ca -create_serial -out {ca_name}/cacert.pem -days 2000 -batch -keyfile {ca_name}/private/cakey.pem -selfsign -extensions v3_ca -infiles {ca_name}/careq.pem'.format(ca_name=ca_name))
    shutil.copy('%s/cacert.pem' % ca_name, 'cacert.pem')
    os.chdir(cwd)
    return ret == 0


def create_ssl(my_dir, ssl_config, ca_dir='etc/ca', ca_name='demoCA'):
    try:
        os.makedirs(my_dir)
    except:
        pass  # may be created, that is fine
    cwd = os.getcwd()
    os.chdir(ca_dir)

    #ret = os.system('openssl genrsa -des3 -out my.key -passout pass:')
    #print('openssl genrsa -des3 -out my.key -passout pass:')
    #if ret != 0:
    #    os.chdir(cwd)
    #    return False

    print(1)
    subj = ssl_config.replace('\n', '/')
    ret = os.system('openssl req -new -nodes -batch -subj "%s" -out newreq.pem -passout pass:' % subj)
    print('openssl req -new -nodes -batch -subj "%s" -out newreq.pem -passout pass:' % subj)
    if ret != 0:
        os.chdir(cwd)
        return False
    print(2)

    ret = os.system('openssl ca -policy policy_anything -batch -out newcert.pem -infiles newreq.pem')
    os.chdir(cwd)
    return ret == 0
