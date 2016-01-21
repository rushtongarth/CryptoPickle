# Crypto Pickle
Cryptographic Python Pickles with gnupg 

## Basic Usage
    >>> import os
    >>> import CryptoPickle
    >>> you = 'keyuser'
    >>> thisloc = '/path/to/gnupg/keys'
    >>> info_object = cryptoPickle.storageinfo()
    >>> info_object_call = info(keyuser=you,loc=thisloc)
    Password:
    >>> cyp = cryptoPickle.CryptoPickle(info_object_call)
    >>> k = cyp.getkeys()
    >>> print k
    ['Key1','Key2',...,'KeyN']