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
import shutil

import yaml

__version__ = '0.0.1+'

config = None

descriptive_names = {}
dependencies = defaultdict(set)
# container dependencies extracted from links and dependencies.yml
role_containers = defaultdict(list)
container_role = defaultdict(str)
container_order = []  # A possible container order
requirements = defaultdict(dict)
descriptive_requirements = {
    'ca': 'Certificate Authority',
    'ssl': 'SSL key and ceritificate'
}

_config_exts = ['.sample', '.link']


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
    requirements = defaultdict(dict, yaml.load(open('containers.yml')))


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
    '''Checks dependencies and gets some metadata.'''
    with open('dependencies.yml') as explicit_dependencies:
        deps = yaml.load(explicit_dependencies)
        for docker_name, server_dependencies in deps.items():
            dependencies[docker_name] = set(server_dependencies)
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
                            dependencies[name].add(docker_name)


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


def is_ssl_configured(container):
    if os.path.exists('etc/%s/ssl.key.pem' % container) and \
            os.path.exists('etc/%s/ssl.cert.pem' % container):
        return True
    return False


def is_requirement_fullfiled(container, req):
    if req == 'ca':
        return True
    elif req == 'ssl':
        return is_ssl_configured(container)
    return False


def all_requirements_done(container):
    for req in requirements[container]:
        if not is_requirement_fullfiled(container, req):
            return False
    return True


def is_configuration_complete(container):
    return all_files_configured(container) and all_requirements_done(container)


def all_containers_configured():
    for container in config['General']['containers']:
        if not is_configuration_complete(container):
            return False
    return True


def _copy(orig, container, fname, check):
    copy = 'docker/%s/copy/%s' % (container, fname[1:])
    named = 'docker/%s/named/%s' % (container, fname[1:])
    if check:
        return os.path.exists(copy) or os.path.exists(named)
    try:
        shutil.copy(orig, copy)
    except:
        shutil.copy(orig, named)


def _copy_ca_artefact(container, artefact, fname, check=False):
    if artefact == 'certificate':
        return _copy('etc/ca/cacert.pem', container, fname, check)
    raise Exception('Unknown artefact %s' % artefact)


def _copy_ssl_artefact(container, artefact, fname, check=False):
    if artefact == 'certificate':
        return _copy('etc/%s/ssl.cert.pem' % container,
                     container, fname, check)
    elif artefact == 'key':
        return _copy('etc/%s/ssl.key.pem' % container,
                     container, fname, check)
    raise Exception('Unknown artefact %s' % artefact)


def generate_configuration():
    for container, services in requirements.items():
        shutil.copy('etc/ssh/authorized_keys', 'docker/%s' % container)
        for service, artefacts in services.items():
            for artefact, files in artefacts.items():
                for fname in files:
                    if service == 'ssl':
                        _copy_ssl_artefact(container, str(artefact), fname)
                    elif service == 'ca':
                        _copy_ca_artefact(container, str(artefact), fname)


def all_configurations_copied():
    for container, services in requirements.items():
        print(container, services)
        if not os.path.exists('docker/%s' % container):
            return False
        for service, artefacts in services.items():
            for artefact, files in artefacts.items():
                for fname in files:
                    if service == 'ssl':
                        ret = _copy_ssl_artefact(
                            container, str(artefact), fname, True)
                    elif service == 'ca':
                        ret = _copy_ca_artefact(container,
                                                str(artefact), fname, True)
                    if not ret:
                        return False
    return True


def _get_link_path(link_redir):
    '''Get a link to another place for a config file.

    Currently only configuration for other containers is supported.'''
    info = yaml.load(open(link_redir))['container']
    my_fname = 'docker/%s/copy/%s' % (info['name'], info['file'])
    return my_fname


def check_copies(checkup):

    def check_cases(cases):
        for case in cases:
            machine = case.split('/')[1]
            root = case[:-7]
            checkup[machine].append((os.path.isfile(root), dest, 'copy'))
    samples = glob.glob('docker/**/*sample', recursive=True)
    check_cases(samples)
    links = glob.glob('docker/**/*link', recursive=True)
    check_cases(links)
    return checkup


def deploy(my_dir, check_instead=False):
    samples = glob.glob('ansible/roles/**/vars/main.yml')
    print(list(requirements.keys()), samples, os.getcwd())
    checkup = defaultdict(list)
    links = []
    for sample in samples:
        host = sample.split('/')[2]
        if host not in requirements:
            continue
        conf = yaml.load(open(sample))
        print(9999, sample, conf)
        for k, container_dir in conf.items():
            if not k.endswith('_dir'):
                continue
            machine = k[:-4]
            print(my_dir, machine)
            if not check_instead:
                try:
                    os.mkdir(my_dir + '/' + machine)
                except FileExistsError:
                    pass  # OK
            for sample_dir, dirs, fnames in os.walk(
                    'docker/%s/named' % machine):
                root = '/'.join([my_dir, machine] + sample_dir.split('/')[3:])
                if not check_instead:
                    for in_dir in dirs:
                        try:
                            print(root, in_dir)
                            os.mkdir(root + '/' + in_dir)
                        except FileExistsError:
                            pass  # OK
                for fname in fnames:
                    if fname.endswith('.sample') or \
                       fname.endswith('.sample.doc') or fname == '.gitignore':
                        continue
                    if fname.endswith('.link'):
                        links.append((
                            _get_link_path(sample_dir + '/' + fname),
                            root + '/' + fname[:-5]))
                        continue
                    print(sample_dir + '/' + fname, root)
                    dest = root + '/' + fname
                    if check_instead:
                        checkup[machine].append((os.path.isfile(dest),
                                                 dest, 'file'))
                    else:
                        shutil.copyfile(sample_dir + '/' + fname,
                                        root + '/' + fname)
    for source, dest in links:
        if check_instead:
            checkup[machine].append((os.path.isfile(dest), dest, 'link'))
        else:
            shutil.copyfile(source, dest)
    if check_instead:
        return check_copies(checkup)


def deploy_on_volumes():
    my_dir = config['General']['nameddirectoriesroot']
    deploy(my_dir)


def check_deployment():
    my_dir = config['General']['nameddirectoriesroot']
    return deploy(my_dir, check_instead=True)


def get_available_options():
    options = [('Basic options', '/')]
    if 'General' in config:
        options.append(('Choose containers', '/choose'))
        if 'containers' in config['General']:
            options.append(('Configure Containers', '/configure'))
            if all_containers_configured():
                options.append(('Generate configuration files', '/generate'))
                if all_configurations_copied():
                    options.append(('Deploy on volumes', '/deploy'))
                    options.append(('Check deployment', '/check_deployment'))
    return options


def link_existing_configuration():
    exiting_confs = glob.glob('_instance/docker', recursive=True)
    for existing_conf in _existing_confs:
        root_name = existing_conf[10:]
        is_config = False
        for ext in _config_exts:
            if os.path.exists(root_name + ext):
                is_config = True
                break
        if not is_config:
            continue
        ext_name = root + ext
        try:
            os.remove(ext_name)
        except OSError:
            pass  # This is OK, file does not exist yet
        os.link(existing_conf, ext_name)
        # Docker does not allow symlinks


def link_ansible():
    try:
        os.mkdir('_instance/ansible')
    except OSError:
        pass  # Fine, already exists
    if not os.path.exists('_instance/ansible/main.yml'):
        shutil.copyfile('ansible/main.yml.example', '_instance/ansible/main.yml')
    if not os.path.exists('_instance/ansible/roles'):
        os.symlink('ansible/roles', '_instance/ansible/roles')


def prepare_instance():
    try:
        os.mkdir('_instance')
    except OSError:
        pass  # Fine, already exists
    link_ansible()
    link_existing_configuration()


load_config()
load_requirements()
get_server_dependencies()
container_order = compute_container_order()
prepare_instance()
