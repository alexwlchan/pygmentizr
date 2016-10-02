# -*- encoding: utf-8 -*-

import collections

import pygments
from pygments.formatters import HtmlFormatter

from pygmentizr import app


RenderOptions = collections.namedtuple('RenderOptions', ['inline'])


def lexer_name_to_lexer(lexer_name):
    """
    Given the name of a lexer
    """


def render_code(code_str, lexer, options=None):
    """
    Takes a string of code and a lexer, and returns a rendered HTML string.
    """
    formatter = HtmlFormatter(
        noclasses=options.inline,
        style=app.config['PYGMENTS_STYLE']
    )
    return pygments.highlight(code_str, lexer(), formatter)