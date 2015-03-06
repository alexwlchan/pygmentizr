from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

import pygment_utils

app = Flask(__name__, template_folder="")
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
        print "Going through!"
        html_output = pygment_utils.render_code("hello", "Python")
        return render_template("index.html",
                               form=form,
                               html_output=html_output)
    else:
        print "Form not validating"

    return render_template("index.html",
                           form=form)

if __name__ == '__main__':
    app.run()