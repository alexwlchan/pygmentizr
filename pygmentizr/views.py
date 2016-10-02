# -*- encoding: utf-8 -*-

from flask import render_template
from pygments.formatters import HtmlFormatter

from pygmentizr import app, forms
from pygmentizr.renderer import render_code


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SnippetForm()

    if form.validate_on_submit():

        try:
            lexer = app.config['SELECTED_LEXERS'][form.language.data]
        except KeyError:
            raise ValueError('Unrecognised language %s' % form.language.data)

        html_output = render_code(
            code_str=form.code.data,
            lexer=lexer,
            style=form.style.data,
        )

        # Get the CSS used by this style to include on the page
        css = HtmlFormatter(
            style=app.config['PYGMENTS_STYLE']
        ).get_style_defs()

        return render_template(
            'index.html',
            form=form,
            html_output=html_output,
            css=css
        )

    return render_template(
        'index.html',
        form=form
    )
