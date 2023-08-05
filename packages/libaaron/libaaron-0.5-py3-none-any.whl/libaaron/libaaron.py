import functools
import typing as t


class reify:
    """ Use as a class method decorator.  It operates almost exactly like the
    Python ``@property`` decorator, but it puts the result of the method it
    decorates into the instance dict after the first call, effectively
    replacing the function it decorates with an instance variable.  It is, in
    Python parlance, a non-data descriptor.

    Stolen from pyramid.
    http://docs.pylonsproject.org/projects/pyramid/en/latest/api/decorator.html#pyramid.decorator.reify
    """

    def __init__(self, wrapped: t.Callable):
        self.wrapped = wrapped
        functools.update_wrapper(self, wrapped)

    def __get__(self, inst, objtype=None):
        if inst is None:
            return self
        val = self.wrapped(inst)
        setattr(inst, self.wrapped.__name__, val)
        return val


def cached(method) -> property:
    """alternative to reify and property decorators. caches the value when it's
    generated. It cashes it as _methodname.
    """
    name = '_%s' % method.__name__

    @property
    def wrapper(self):
        try:
            return getattr(self, name)
        except AttributeError:
            val = method(self)
            setattr(self, name, val)
            return val
    return wrapper


def w(iterable: t.Iterable) -> t.Iterable:
    """yields from an iterable with its context manager."""
    with iterable:
        yield from iterable


class DotDict(dict):
    "dict for people who are too lazy to type brackets and quotation marks"
    __slots__ = ()
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __dir__(self):
        return list(self)
 

def flatten(iterable: t.Iterable, map2iter: t.Callable=None) -> t.Iterator:
    """recursively flatten nested objects"""
    if map2iter and isinstance(iterable, t.Mapping):
        iterable = map2iter(iterable)

    for item in iterable:
        if isinstance(item, str) or not isinstance(item, t.Iterable):
            yield item
        else:
            yield from flatten(item, map2iter)
