# aio-timers

[![PyPI - License](https://img.shields.io/pypi/l/aio-times.svg?longCache=true&&style=flat-square)](https://github.com/ThierrySpetebroot/aio-timers/blob/master/LICENSE)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aio-times.svg?longCache=true&&style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/aio-times.svg?longCache=true&&style=flat-square)](https://test.pypi.org/project/aio-timers/)


Timing utilities based on `asyncio`.

## Setup
`pip install aio-timers`

## Usage
```python
import asyncio
from aio_timers import Timer

def callback(name):
    print("Hello {}!".format(name))

# timer is scheduled here
timer = Timer(5, callback, callback_args=("World",))

# wait until the callback has been executed
loop = asyncio.get_event_loop()
loop.run_until_complete(timer.wait())
print("end")
```

Output:

(after 5 seconds)
> Hello World!
>
> end

### Timer

Calls a `callback` after `delay` seconds.

The timer is executed as a task on an event loop.

The callback is invoked:
 - as a synchronous function if it is not a coroutine;
 - with an await if it is a coroutine or the `callback_async` flag is set to `True`.

Any result returned by the callback is ignored.

#### Constructor
`Timer(delay, callback, callback_args=(), callback_kwargs={}, callback_async=False, *, loop=None)`

where:
 - delay, seconds before the `callback` is executed;
 - callback, the callback to execute after `delay` seconds
 - callback_args, (optional, default=`()`) positional arguments to pass to `callback`
 - callback_kwargs, (optional, default=`{}`) keyword arguments to pass to `callback`
 - callback_async, (optional, default=`False`) if `True` the callback will be executed on the event loop (`await`)
 - loop, (optional, default=`None`) event loop where the delayed task will be scheduled (if`None` will use `asyncio.get_event_loop()`)

NOTE: the `callback_async` flag should be used when a coroutine is decorated (e.g., using `functools.partial`)

#### .cancel()
Cancels the execution of the callback.

#### async .wait()
Wait until the callback has been executed or its execution has been canceled.

If the execution has been canceled, will raise `asyncio.CancelledError`.
