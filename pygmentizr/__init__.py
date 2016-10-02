# -*- encoding: utf-8 -*-

from flask import Flask

__version__ = '0.1'

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'how-not-to-be-seen'

from pygmentizr import pygmentizr
