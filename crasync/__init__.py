import asyncio
from multimple import multimple

__version__ = '0.0'


def crasync(arg):
    if isinstance(arg, type):
        klass = multimple(arg)
        setattr(klass, 'async', klass.multimple('async'))
        setattr(klass, 'sync', klass.multimple('sync'))

        return klass
    else:
        async_func = arg

        # TODO: check function aync-ness
        def sync_func(*args, **kwargs):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            future = async_func(*args, **kwargs)

            return loop.run_until_complete(future)

        imo = multimple('async')(async_func)
        imo.multimple('sync')(sync_func)

        return imo
