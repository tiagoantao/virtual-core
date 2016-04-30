# -*- coding: utf-8 -*-
'''
.. module:: wizard.__main__
   :synopsis: A Web based wizard to setup the core, entry point
   :noindex:
   :copyright: Copyright 2016 by Tiago Antao
   :license: GNU Affero, see LICENSE for details

.. moduleauthor:: Tiago Antao <tra@popgen.net>

'''
import os
import socket

from flask import Flask, render_template, redirect, request, url_for

import wizard
from wizard import ca

app = Flask(__name__)

_ca_template = '''
[ req ]
default_bits           = 2048
distinguished_name     = req_distinguished_name
attributes             = req_attributes
prompt                 = no

[ req_distinguished_name ]
countryName            = {country}
stateOrProvinceName    = {state}
localityName           = {locality}
organizationName       = {orgname}
organizationalUnitName = {orgunit}
commonName             = {commonname}
emailAddress           = {email}

[ req_attributes ]
'''


def _delist(form, exceptions=[]):
    delist = {}
    for k, v in form.items():
        if type(v) == list and k not in exceptions:
            delist[k] = v[0]
        else:
            delist[k] = v
    return delist


def _has_all_parameters(form, parameters):
    for parameter in parameters:
        if parameter in form:
              if form[parameter] == '':
                  return False
        else:
            return False
    return True


@app.route('/', methods=['GET'])
@app.route('/<int:run>', methods=['GET', 'POST'])
def welcome(run=0):
    if run == 0:
        form = wizard.config.get('General', {})
    else:
        form = _delist(request.form)
        if _has_all_parameters(form, ['host', 'country', 'state', 'locality', 'orgname', 'orgunit', 'commonname', 'email']):
            wizard.change_config('General', **form)
            return redirect(url_for('determine_ssh_status', run=0))
    if 'host' not in form:
        form['host'] = socket.getfqdn()
    all_params = {'run': run, **form}
    return render_template('welcome.html', **all_params)


@app.route('/sshkey/<int:run>')
def determine_ssh_status(run=0):
    if not os.path.exists('etc/ssh'):
        os.mkdir('etc/ssh')
    if not os.path.exists('etc/ssh/authorized_keys'):
        return render_template('need_ssh.html', run=run)
    else:
        return redirect(url_for('explain_certificate_authority', run=0))


@app.route('/ca/<int:run>')
def explain_certificate_authority(run=0):
    # TODO: this needs to be changed
    if not os.path.exists('etc/ca'):
        os.mkdir('etc/ca')
    if not os.path.exists('etc/ca/UNDERSTAND') and \
            not os.path.exists('etc/ca/demoCA'):
        return render_template('need_ca.html', run=run)
    else:
        return redirect(url_for('get_named_directories_root'))


@app.route('/create_ca')
def create_certificate_authority(run=0):
    if os.path.exists('etc/ca/demoCA'):
        return render_template('exists_ca.html', next_route='/named_directories')
    ca_template = _ca_template.format(
        country=wizard.config['General']['country'],
        state=wizard.config['General']['state'],
        locality=wizard.config['General']['locality'],
        orgname=wizard.config['General']['orgname'],
        orgunit=wizard.config['General']['orgunit'],
        commonname=wizard.config['General']['commonname'],
        email=wizard.config['General']['email'])
    with open('init.ssl', 'wt') as w:
        w.write(ca_template)
    ca_ok = ca.create_ca()
    if ca_ok:
        return redirect(url_for('get_named_directories_root'))
    return render_template('ca_not_created.html')


@app.route('/named_directories', methods=['GET','POST'])
def get_named_directories_root():
    form = _delist(request.form)
    if 'named' in form:
        root = form['named']
    else:
        root = wizard.config['General'].get('nameddirectoriesroot', None)
    if root is None or not os.path.isdir(root):
        return render_template('named_directories.html', root=root)
    wizard.change_config('General', nameddirectoriesroot=root)
    return redirect(url_for('choose_containers'))


@app.route('/choose')
def choose_containers():
    return render_template('choose_containers.html',
        descriptive_names=wizard.descriptive_names,
        dependencies=wizard.dependencies,
        role_containers=wizard.role_containers,
        container_order=wizard.container_order)

if __name__ == "__main__":
    app.debug = True
    app.run()
