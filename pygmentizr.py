from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

import choices

app = Flask(__name__, template_folder="")
app.config.from_object('config')

#------------------------------------------------------------------------------
# Form for handling code snippets
#------------------------------------------------------------------------------
class SnippetForm(Form):
    language = SelectField('language',
                           validators=[DataRequired()],
                           choices=choices.form_choices(),
                           coerce=int)
    code = TextAreaField('code_snippet', validators=[DataRequired()])
    inline = BooleanField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SnippetForm()

    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run()