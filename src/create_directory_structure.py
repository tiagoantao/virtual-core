import glob
import sys

import yaml

if len(sys.argv) != 2:
    print('Syntax: %s <base_dir>' % sys.argv[0])
    sys.exit(-1)
else:
    my_dir = sys.argv[1]

replace = '/path_to_'

samples = glob.glob('ansible/roles/**/vars/main.yml')
for sample in samples:
    conf = yaml.load(open(sample))
    print(conf)
