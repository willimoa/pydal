import sys
import hashlib
import os

PY2 = sys.version_info[0] == 2

if PY2:
    import cPickle as pickle
    import cStringIO as StringIO
    import copy_reg as copyreg
    hashlib_md5 = hashlib.md5
    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
    integer_types = (int, long)
else:
    import pickle
    from io import StringIO
    import copyreg
    hashlib_md5 = lambda s: hashlib.md5(bytes(s, 'utf8'))
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())
    integer_types = (int,)


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


# shortcuts
pjoin = os.path.join
exists = os.path.exists
ogetattr = object.__getattribute__
osetattr = object.__setattr__
