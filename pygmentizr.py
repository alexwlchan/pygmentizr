from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

import pygment_utils

app = Flask(__name__)
app.config.from_object('config')

#------------------------------------------------------------------------------
# Form for handling code snippets
#------------------------------------------------------------------------------
class SnippetForm(Form):
    language = SelectField('language',
                           validators=[DataRequired()],
                           choices=pygment_utils.form_choices(),
                           coerce=int)
    code = TextAreaField('code_snippet', validators=[DataRequired()])
    inline = BooleanField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SnippetForm()

    if form.validate_on_submit():
        html_output = pygment_utils.render_code(form.code.data,
                                                form.language.data,
                                                form.inline.data)
        return render_template("index.html",
                               form=form,
                               html_output=html_output)

    return render_template("index.html",
                           form=form)

if __name__ == '__main__':
    app.run()