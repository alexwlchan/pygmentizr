# -*- encoding: utf-8 -*-

import collections

import pygments
from pygments.formatters import HtmlFormatter

from pygmentizr import app


STYLE_OPTIONS = [
    'Use CSS classes',
    'Apply inline CSS styles',
    'For Metacom',
]


def render_code(code_str, lexer, style):
    """
    Takes a string of code and a lexer, and returns a rendered HTML string.
    """
    if style in ('Apply inline CSS styles', 'For Metacom'):
        noclasses = True
    else:
        noclasses = False

    formatter = HtmlFormatter(
        noclasses=noclasses,
        style=app.config['PYGMENTS_STYLE']
    )
    highlighted_string = pygments.highlight(code_str, lexer(), formatter)

    return highlighted_string