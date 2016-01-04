#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Stephen Garth <stephen.r.garth@vanderbilt.edu>'
__copyright__ = 'Copyright 2015 Vanderbilt University. All Rights Reserved'
__desc__ = 'CryptoPickle is a cryptographic method of storing python pickles'
#
# Package analogous to CLI of 'gpg' but using python
#
# cryptoPickle/__init__.py
from cryptoPickle import *


VERSION = (0,0,1)

def get_version():
	return '.'.join(str(i) for i in VERSION)

__version__ = get_version()

