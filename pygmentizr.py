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

SELECTED_LEXERS = [
    ('PythonLexer', 'Python'),
    ('CoffeeScriptLexer', 'CoffeeScript'),
    ('CssLexer', 'CSS'),
    ('PythonConsoleLexer', 'Python console')
]

# Select the style used by Pygments
PYGMENTS_STYLE = 'default'

#------------------------------------------------------------------------------
# Set up the Flask app
#------------------------------------------------------------------------------
app = Flask(__name__, template_folder='', static_url_path='', static_folder='')

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'how-not-to-be-seen'

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
                                            style=PYGMENTS_STYLE))

#------------------------------------------------------------------------------
# Form for handling code snippets
#------------------------------------------------------------------------------
class SnippetForm(Form):
    language = SelectField('language',
                           validators=[DataRequired()],
                           choices=SELECTED_LEXERS)
    code = TextAreaField('code_snippet', validators=[DataRequired()])
    inline = BooleanField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SnippetForm()

    if form.validate_on_submit():
        html_output = render_code(form.code.data,
                                  form.language.data,
                                  form.inline.data)

        # Get the CSS used by this style to include on the page
        css = HtmlFormatter(style=PYGMENTS_STYLE).get_style_defs()

        return render_template("index.html",
                               form=form,
                               html_output=html_output,
                               css=css)

    return render_template("index.html",
                           form=form)

if __name__ == '__main__':
    app.run()
