# -*- encoding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

from pygmentizr import app


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
    inline = BooleanField()
