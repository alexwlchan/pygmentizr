# -*- encoding, utf-8 -*-

from collections import OrderedDict
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'Pygments is a generic syntax highlighter'
)

# Select the lexers to be exposed in the interface
from pygments.lexers import *

SELECTED_LEXERS = OrderedDict([
    ('Python',          PythonLexer),
    ('Python console',  PythonConsoleLexer),
    ('Plain text',      TextLexer),
    ('C',               CLexer),
    ('C++',             CppLexer),
    ('Bash/Ksh',        BashLexer),
    ('Bash console',    BashSessionLexer),
    ('Go',              GoLexer),
    ('Rust',            RustLexer),
    ('JavaScript',      JavascriptLexer),
    ('JSON',            JsonLexer),
    ('XML',             XmlLexer),
    ('Diff',            DiffLexer),
])

# Select the style used by Pygments
PYGMENTS_STYLE = 'default'
