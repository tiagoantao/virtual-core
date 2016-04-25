import os


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
    print('openssl req -new -keyout {complete_dir}/private/cakey.pem -config input -nodes -out {complete_dir}/careq.pem'.format(complete_dir=complete_dir))
    # 2000 is number of days (arbitrary, really)
    cwd = os.getcwd()
    os.chdir(my_dir)
    print('openssl ca -create_serial -out {ca_name}/cacert.pem -days 2000 -batch -keyfile {ca_name}/private/cakey.pem -selfsign -extensions v3_ca -infiles {ca_name}/careq.pem'.format(ca_name=ca_name))
    os.chdir(cwd)


create_ca()
