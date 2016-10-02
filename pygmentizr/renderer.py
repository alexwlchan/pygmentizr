# -*- encoding: utf-8 -*-

import pygments
from pygments.formatters import HtmlFormatter

from pygmentizr import app


STYLE_OPTIONS = [
    'Use CSS classes',
    'Apply inline CSS styles',
    'For Metacom',
]


def metacom_code(hilite_str):
    """
    Apply special styling for rendering code on Metacom.
    """
    # Remove the opening and closing <div> tags
    opening = '<div class="highlight" style="background: #f8f8f8">'
    closing = '</div>'
    hilite_str = hilite_str[len(opening):-len(closing)-1].strip()

    # Temporarily remove the opening/closing <pre> tags
    opening_pre = '<pre style="line-height: 125%">'
    closing_pre = '</pre>'
    hilite_str = hilite_str[len(opening_pre):-len(closing_pre)-1].strip()

    # Turn off that horrific green coloring from Jive.
    opening_pre = '<pre style="line-height: 125%; color: #3d3d3d;">'

    # Go through and add <code> tags to each line
    hilite_str = '<br/>\n'.join(
        '<code>%s</code>' % line if line.strip() else ''
        for line in hilite_str.splitlines()
    )

    # Re-add the opening/closing <pre> tags
    hilite_str = opening_pre + hilite_str + closing_pre

    return hilite_str


def render_code(code_str, lexer, style):
    """
    Takes a string of code and a lexer, and returns a rendered HTML string.
    """
    noclasses = (style in ('Apply inline CSS styles', 'For Metacom'))

    formatter = HtmlFormatter(
        noclasses=noclasses,
        style=app.config['PYGMENTS_STYLE']
    )
    highlighted_string = pygments.highlight(code_str, lexer(), formatter)

    return highlighted_string