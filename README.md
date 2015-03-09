# pygmentizr

Pygmentizr is a web app that takes code, and returns HTML with syntax colouring, using the [Pygments library][1].

For motivation, see the [accompanying blog post][2].

## Installation

Clone or download this repository, then install the requirements with pip:

    git clone git@github.com:alexwlchan/pygmentizr.git
    cd pygmentizr
    pip install -r requirements.txt

## Configuration

The list of lexers/language choices is specified in `pygmentizr.py`. Here's an example:

```python
from pygments.lexers import *

SELECTED_LEXERS = [
    ('PythonLexer', 'Python'),
    ('CoffeeScriptLexer', 'CoffeeScript'),
    ('CssLexer', 'CSS'),
    ('PythonConsoleLexer', 'Python console')
]
```

For each language you want to include, add a tuple to `SELECTED_LEXERS`. The first item should be the Lexer, and the second the name of the language to appear in the list of available languages.

The lexers don't have to be part of the Pygments library. Any Pygments-style lexer can be used here, as long as it's been appropriately imported first.

You can also use any theme which you've imported: just change the value of `PYGMENTS_STYLE` to the name of the style as a string.

## Running the app

Just run the pygmentizr script:

```bash
cd pygmentizr
python pygmentizr.py
```

This starts the Flask instance which runs Pygmentizr. Point a web browser at <http://localhost:5000> to use the app.

## Acknowledgements

The favicon is the [fa-code icon][3] from the [Font Awesome][4] toolkit.

[1]: http://pygments.org
[2]: http://www.alexwlchan.net/2015/03/pygmentizr
[3]: http://fortawesome.github.io/Font-Awesome/icon/code/
[4]: http://fortawesome.github.io/Font-Awesome/