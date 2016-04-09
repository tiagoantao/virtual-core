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

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/sshkey')
def determine_ssh_status(run=0):
    if not os.path.exists('etc/ssh'):
        os.mkdir('etc/ssh')
    if not os.path.exists('etc/ssh/authorized_keys'):
        return render_template('need_ssh.html', run=run)
    else:
        return redirect(url_for(choose_machines))


@app.route('/choose')
def choose_machines():
    return 'bla'


if __name__ == "__main__":
    app.debug = True
    app.run()
