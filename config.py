# -*- encoding, utf-8 -*-

from collections import OrderedDict

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Pygments is a generic syntax highlighter'

# Select the lexers to be exposed in the interface
from pygments.lexers import *

SELECTED_LEXERS = OrderedDict([
    ('Python',           PythonLexer),
    ('Python console',   PythonConsoleLexer),
    ('CoffeeScript',     CoffeeScriptLexer),
    ('CSS',              CssLexer),
])

# Select the style used by Pygments
PYGMENTS_STYLE = 'default'
