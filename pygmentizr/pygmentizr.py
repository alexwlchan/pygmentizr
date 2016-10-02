# -*- encoding: utf-8 -*-

from pygmentizr import app

from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

#------------------------------------------------------------------------------
# CONFIGURATION
#
# Define the list of lexers you want to use.
#
# Lexers should be entered as a tuple in SELECTED_LEXERS, with the first
# entry being the Lexer class, and the second entry the name of the language
# you want to show up in the language chooser. Languages will appear in this
# order in the form.
#------------------------------------------------------------------------------
import pygments
from pygments.lexers import *
from pygments.formatters import HtmlFormatter

#------------------------------------------------------------------------------
# Utility functions for rendering code
#------------------------------------------------------------------------------
def render_code(code, lexer_name, inline=False):
    """Takes a string of code and the name of a lexer, and returns a rendered
    HTML string.

    If inline is true, it uses inline styles to render the text rather than
    CSS classes. This is useful for environments where external stylesheets are
    unavailable (e.g. email).
    """
    # The lexer name comes from the choices from the SelectField in SnippetForm
    # so can probably be trusted - even so, we have to be a little careful here.
    lexer = globals()[lexer_name]

    return pygments.highlight(code,
                              lexer(),
                              HtmlFormatter(noclasses=inline,
                                            style=app.config['PYGMENTS_STYLE']))

#------------------------------------------------------------------------------
# Form for handling code snippets
#------------------------------------------------------------------------------
