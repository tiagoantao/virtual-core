# -*- coding: utf-8 -*-
'''
.. module:: wizard
   :synopsis: A Web based wizard to setup the core
   :noindex:
   :copyright: Copyright 2016 by Tiago Antao
   :license: GNU Affero, see LICENSE for details

.. moduleauthor:: Tiago Antao <tra@popgen.net>

'''
from collections import defaultdict
import glob
import os

import yaml

__version__ = '0.0.1+'

config = None

descriptive_names = {}
dependencies = defaultdict(list)  # container dependencies extracted from links
role_containers = defaultdict(list)
container_role = defaultdict(str)
container_order = []  # A possible container order
requirements = defaultdict(list)
descriptive_requirements = {
    'ca': 'Certificate Authority',
    'ssl': 'SSL key and ceritificate'
}


def load_config():
    '''Loads configuration from a previous execution.
    '''
    global config
    try:
        config = yaml.load(open('virtual-core.yml'))
    except FileNotFoundError:
        config = {}


def load_requirements():
    '''Loads container requirements.
    '''
    global requirements
    requirements = yaml.load(open('containers.yml'))


def save_config():
    '''Saves configuration.
    '''
    w = open('virtual-core.yml', 'wt')
    w.write(yaml.dump(config, default_flow_style=False))
    w.close()


def change_config(section, **kwargs):
    if section not in config:
        config[section] = {}
    for k, v in kwargs.items():
        config[section][k] = v
    save_config()


def get_server_dependencies():
    main_roles = glob.glob('ansible/roles/**/tasks/main.yml')
    for main_role in main_roles:
        role = main_role.split('/')[2]
        with open(main_role) as f:
            doc = yaml.load(f)
            for entry in doc:
                if 'docker' in entry:
                    descriptive_name = entry['name']
                    name = entry['docker']['name']
                    role_containers[role].append(name)
                    container_role[name] = role
                    descriptive_names[name] = descriptive_name
                    if 'links' in entry['docker']:
                        for link in entry['docker']['links']:
                            docker_name, internal_name = tuple(link.split(':'))
                            dependencies[name].append(docker_name)


def compute_container_order(done=set(['ldap'])):
        if len(done) == 1:
            container_order = ['ldap']
        else:
            container_order = []
        for container, deps in dependencies.items():
            if container in done:
                continue
            done.add(container)
            pre_containers = compute_container_order(done)
            container_order.append(container)
            container_order.extend(pre_containers)
        return container_order


def get_all_dependencies(container):
    '''Returns all containers that are required by a certain container
    '''
    my_dependencies = []
    check_containers = [container]
    while check_containers is not []:
        check_dependencies = dependencies[check]
        check_containers.extend(check_dependencies)
        my_dependencies.extend(check_containers)
        del check_containers[container]
    return my_dependencies


def get_configuration_file_samples(container):
    samples = glob.glob('docker/%s/**/*sample' % container, recursive=True)
    return samples


def is_file_configured(container, file_name):
    final_name = file_name[:-7]
    if os.path.exists(final_name):
        return True
    return False


def all_files_configured(container):
    for file_name in get_configuration_file_samples(container):
        if not is_file_configured(container, file_name):
            return False
    return True


def is_configuration_complete(container):
    return all_files_configured(container)

load_config()
load_requirements()
get_server_dependencies()
container_order = compute_container_order()
