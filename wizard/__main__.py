# -*- coding: utf-8 -*-
'''
.. module:: wizard.__main__
   :synopsis: A Web based wizard to setup the core, entry point
   :noindex:
   :copyright: Copyright 2016 by Tiago Antao
   :license: GNU Affero, see LICENSE for details

.. moduleauthor:: Tiago Antao <tra@popgen.net>

'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run()
