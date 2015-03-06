import pygments
from pygments.formatters import HtmlFormatter

from config import SELECTED_LEXERS

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

def lexer_choice(form_choice):
    """Returns the lexer corresponding to the int from the form choice."""
    # Remember that the form choice array is indexed from 1, so we need to
    # adjust the index appropriately.
    language_tuple = SELECTED_LEXERS[form_choice - 1]

    return language_tuple[0]

def render_code(code, language_code, inline=False):
    """Takes a string of code and a lexer, and returns a rendered HTML string.

    If inline is true, it uses inline styles to render the text rather than
    CSS classes. This is useful for environments where external stylesheets are
    unavailable (e.g. email).
    """
    lexer = lexer_choice(language_code)

    return pygments.highlight(code, lexer(), HtmlFormatter(noclasses=inline))