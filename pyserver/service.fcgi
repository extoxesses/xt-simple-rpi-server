#!/usr/bin/python

import logging
import os
import sys
from flup.server.fcgi import WSGIServer
from src.server import app

# TODO: Set server foler path
server_path = ''

# Virtual env configuration
logging.basicConfig(stream=sys.stderr)
os.system(f'source /var/www/{server_path}/.venv/bin/activate')
sys.path.insert(0,f'/var/www/{server_path}/')

# WSGI server start
if __name__ == '__main__':
  WSGIServer(app).run()
