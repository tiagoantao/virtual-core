import glob
import os
import shutil
import sys

import yaml

if len(sys.argv) != 2:
    print('Syntax: %s <base_dir>' % sys.argv[0])
    sys.exit(-1)
else:
    my_dir = sys.argv[1]


def make_dir(my_dir):
    try:
        os.mkdir(my_dir)
    except FileExistsError:
        pass  # This is OK

samples = glob.glob('ansible/roles/**/vars/main.yml')
for sample in samples:
    conf = yaml.load(open(sample))
    for k, container_dir in conf.items():
        if not k.endswith('_dir'):
            continue
        machine = k[:-4]
        print(machine)
        make_dir(my_dir + machine)
        for sample_dir, dirs, fnames in os.walk('docker/%s/conf' % machine):
            root = '/'.join([my_dir, machine] + sample_dir.split('/')[3:])
            for in_dir in dirs:
                make_dir(root +  '/' + in_dir)
            for fname in fnames:
                if fname.endswith('.sample'):
                    continue
                print(sample_dir + '/' + fname, root)
                shutil.copyfile(sample_dir + '/' + fname, root + '/' + fname)
