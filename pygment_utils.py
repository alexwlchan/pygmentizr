from pygments.lexers import *

SELECTED_LEXERS = [
    (PythonLexer, 'Python'),
    (CoffeeScriptLexer, 'CoffeeScript'),
    (CssLexer, 'CSS'),
    (PythonConsoleLexer, 'Python console')
]

def form_choices():
    """Returns a list of tuples suitable for passing as a list of choices
    to SelectField() based upon the list of lexers.
    """
    choices = list()

    for idx, item in enumerate(SELECTED_LEXERS):
        # The first part of the tuple is the index, the second the string
        # displayed in the dropdown. WTFields rejects index 0, so we need to
        # increment everything by 1.
        choices.append((idx + 1, item[1]))

    return choices

def render_code(code, lexer, inline=False):
    """Takes a string of code and a lexer, and returns a rendered HTML string.

    If inline is true, it uses inline styles to render the text rather than
    CSS classes. This is useful for environments where external stylesheets are
    unavailable (e.g. email).
    """
    return "<p>print(\"Hello world\");</p>"