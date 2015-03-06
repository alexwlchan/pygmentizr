WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#------------------------------------------------------------------------------
# Define the list of lexers you want to use.
#
# Lexers should be entered as a tuple in SELECTED_LEXERS, with the first
# entry being the Lexer class, and the second entry the name of the language
# you want to show up in the language chooser. Languages will appear in this
# order in the form.
#------------------------------------------------------------------------------
from pygments.lexers import *

SELECTED_LEXERS = [
    (PythonLexer, 'Python'),
    (CoffeeScriptLexer, 'CoffeeScript'),
    (CssLexer, 'CSS'),
    (PythonConsoleLexer, 'Python console')
]