# -*- coding: utf-8 -*-

"""Top-level package for RLTG."""

__author__ = """Marco Favorito"""
__email__ = 'marco.favorito@gmail.com'
__version__ = '0.1.2.post1'

import logging
logging.getLogger('rltg').addHandler(logging.NullHandler())
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

logger = logging.getLogger('matplotlib')
# set WARNING for Matplotlib
logger.setLevel(logging.WARNING)


