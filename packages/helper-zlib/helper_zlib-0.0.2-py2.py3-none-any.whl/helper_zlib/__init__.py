"""
Reference
 - http://php.net/manual/en/function.gzdeflate.php#69046
 - http://www.php2python.com/wiki/function.gzdeflate/
"""

import zlib
import binascii

def gzdeflate(data, level=zlib.Z_BEST_COMPRESSION):
    """
    >>> binascii.hexlify(gzdeflate('hello world'))
    'cb48cdc9c95728cf2fca490100'
    """
    return gzcompress(data=data, level=level)[2:-4]

def gzinflate(data, wbits=-zlib.MAX_WBITS):
    """
    >>> gzinflate(binascii.unhexlify('cb48cdc9c95728cf2fca490100'))
    'hello world'
    """
    return zlib.decompress(data, wbits)


def gzcompress(data, level=zlib.Z_BEST_COMPRESSION):
    """
    >>> binascii.hexlify(gzcompress('hello world'))
    '78dacb48cdc9c95728cf2fca4901001a0b045d'


    See also
    https://docs.python.org/2/library/codecs.html#standard-encodings

    >>> binascii.hexlify('hello world'.encode('zlib'))
    '789ccb48cdc9c95728cf2fca4901001a0b045d'
    """
    s = zlib.compress(data, level)
    return s

def gzuncompress(data):
    """
    >>> gzuncompress(binascii.unhexlify('78dacb48cdc9c95728cf2fca4901001a0b045d'))
    'hello world'
    """
    return zlib.decompress(data)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
