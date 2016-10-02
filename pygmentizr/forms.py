# -*- encoding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

from pygmentizr import app
from pygmentizr.renderer import STYLE_OPTIONS


class SnippetForm(Form):
    """
    Form for handling code snippets.
    """
    language = SelectField(
        'language',
        validators=[DataRequired()],
        choices=[(k, k) for k in app.config['SELECTED_LEXERS']],
    )
    code = TextAreaField('code_snippet', validators=[DataRequired()])
    style = SelectField(
        'style',
        validators=[DataRequired()],
        choices=[(k, k) for k in STYLE_OPTIONS]
    )

