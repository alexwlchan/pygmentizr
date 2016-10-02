#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Pygmentizr.  A web app for highlighting code with HTML using the
Pygments library.

Usage:
  manage.py run [--debug] [--port=<port>] [--host=<host>]
  manage.py (-h | --help)
  manage.py --version

Options:
  -h --help      Show this screen.
  --version      Show version.
  --debug        Whether to enable debug mode.
  --port=<port>  The port of the webserver.  Defaults to 5000.
  --host=<host>  Hostname to listen on.  Set to 0.0.0.0 to make the server
                 available externally.  Defaults to '127.0.0.1'.
"""

import sys

from docopt import docopt

from pygmentizr import app, __version__


if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)

    is_debug = args['--debug']
    if args['--port'] is not None:
        try:
            port_num = args['--port']
        except ValueError:
            sys.exit('%s is not a valid port number.' % args['--port'])
    else:
        port_num = 5000
    host = args.get('--host', '127.0.0.1')

    app.run(debug=is_debug, port=port_num, host=host)
