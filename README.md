# pygmentizr

Pygmentizr is a web app that takes code, and returns HTML with syntax colouring, using the [Pygments library][1].

For motivation, see the [accompanying blog post][2].

You can try a [live demo](https://alexwlchan.net/experiments/pygmentizr/) of the app.

## Installation

Clone this repository, create a virtualenv, then install the requirements with pip:

```console
$ git clone git@github.com:alexwlchan/pygmentizr.git
$ cd pygmentizr
$ virtualenv env; source env/bin/activate
$ pip install -r requirements.txt
```

## Configuration

The list of lexers/language choices is specified in `config.py`. Here's an example:

```python
from pygments.lexers import *

SELECTED_LEXERS = OrderedDict([
    ('Python',           PythonLexer),
    ('Python console',   PythonConsoleLexer),
    ('CoffeeScript',     CoffeeScriptLexer),
    ('CSS',              CssLexer),
])
```

For each language you want to include, add a tuple to `SELECTED_LEXERS`.
The first item should be the name you want to appear in the interface, the second the lexer object from Pygments.

## Running the app

To run a local instance, invoke as follows:

```console
$ cd /path/to/pygmentizr
$ source env/bin/activate
$ python manage.py run
```

This starts the Flask instance which runs Pygmentizr. Point a web browser at <http://localhost:5000> to use the app.

Alternatively, you can use the Docker implementation:

```console
$ docker build -t alexwlchan/pygmentizr .
$ docker run -p 5000:80 alexwlchan/pygmentizr
```

## Acknowledgements

The favicon is the [fa-code icon][3] from the [Font Awesome][4] toolkit.

[1]: http://pygments.org
[2]: http://www.alexwlchan.net/2015/03/pygmentizr
[3]: http://fortawesome.github.io/Font-Awesome/icon/code/
[4]: http://fortawesome.github.io/Font-Awesome/
