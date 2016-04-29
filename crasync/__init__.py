from multimple import multimple

__version__ = '0.0'


class Crasync(object):
    def __get__(self, owner, klass=None):
        pass

    @classmethod
    def decorator(cls, arg):
        if isinstance(arg, type):
            return cls.class_decorator(arg)
        else:
            return cls.func_decorator(arg)

    @classmethod
    def func_decorator(cls, async_func):
        # TODO: check function aync-ness
        sync_func = cls.make_sync(async_func)

        imo = multimple('async')(async_func)
        imo.multimple('sync')(sync_func)

        return imo

    @classmethod
    def class_decorator(cls, klass):
        return multimple(klass)

    @classmethod
    def make_sync(cls, async_func):
        pass
