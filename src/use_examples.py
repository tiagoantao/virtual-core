# -*- coding: utf-8 -*-
'''
   Uses the example configuration files as the default ones
'''

import glob
import os
import shutil
import time

samples = glob.glob('docker/**/*sample', recursive=True)
for sample in samples:
    root = sample[:-7]
    try:
        root_time = os.path.getmtime(root)
        sample_time = os.path.getmtime(sample)
        if root_time > sample_time:
            print('%s more recent than %s, not changing' % (root, sample))
            continue
    except FileNotFoundError:
        pass
    shutil.copyfile(sample, root)
