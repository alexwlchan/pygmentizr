# -*- encoding: utf-8 -*-

from flask import Flask

__version__ = '0.1'

app = Flask(__name__)
app.config.from_object('config')

from pygmentizr import views
