# -*- coding: utf-8 -*-
'''
    Pre-processes the YAML files as a function of the volume directory.

    Probably not the an approach that can be called "best-practice"
'''
import glob
import sys

import yaml

if len(sys.argv) != 2:
    print('Syntax: %s <base_dir>' % sys.argv[0])
    sys.exit(-1)
else:
    my_dir = sys.argv[1]

replace_str = '/path_to_'


def replace(obj, pattern, replacement):
    if type(obj) == str:
        return obj.replace(pattern, replacement)
    elif type(obj) == list:
        return [e.replace(pattern, replacement) for e in obj]
    raise Exception()

samples = glob.glob('ansible/roles/**/vars/main.yml.sample')
for sample in samples:
    root = sample[:-7]
    print(root)
    conf = yaml.load(open(sample))
    new_conf = {k: replace(v, replace_str, my_dir) for k, v in conf.items()}
    w = open(root, 'wt', encoding='utf-8')
    w.write(yaml.dump(new_conf, default_flow_style=False))
    w.close()
