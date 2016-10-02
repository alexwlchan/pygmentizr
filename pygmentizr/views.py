# -*- encoding: utf-8 -*-

from flask import render_template
from pygments.formatters import HtmlFormatter

from pygmentizr import app, forms
from pygmentizr.pygmentizr import render_code


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SnippetForm()

    if form.validate_on_submit():
        html_output = render_code(
            form.code.data,
            form.language.data,
            form.inline.data
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
