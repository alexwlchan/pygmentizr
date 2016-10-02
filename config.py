# -*- encoding: utf-8 -*-

WTF_CSRF_ENABLED = True

SECRET_KEY = 'Pygments is a generic syntax highlighter suitable'

# Set up the lexers to make available.
SELECTED_LEXERS = [
    ('PythonLexer', 'Python'),
    ('CoffeeScriptLexer', 'CoffeeScript'),
    ('CssLexer', 'CSS'),
    ('PythonConsoleLexer', 'Python console')
]

# Select the style used by Pygments
PYGMENTS_STYLE = 'default'
