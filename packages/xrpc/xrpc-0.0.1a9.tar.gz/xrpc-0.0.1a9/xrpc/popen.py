import base64
import logging
import os
import pickle
import zlib
from contextlib import ExitStack, contextmanager

import signal

import subprocess
import sys
from typing import NamedTuple, Callable, Any, Tuple, Dict, List

from xrpc.util import signal_context


@contextmanager
def cov():
    import coverage

    cov = None
    try:
        cov = coverage.process_startup()
        yield
    finally:
        if cov:
            cov.save()


def argv_encode(x: Any):
    return base64.b64encode(zlib.compress(pickle.dumps(x), level=9)).decode()


def argv_decode(x: Any):
    return pickle.loads(zlib.decompress(base64.b64decode(x)))


class PopenStruct(NamedTuple):
    fn: Callable
    args: Tuple[Any]
    kwargs: Dict[str, Any]


def popen(fn, *args, **kwargs) -> subprocess.Popen:
    args = [
        sys.executable,
        '-m',
        __name__,
        f'{fn.__module__}.{fn.__name__}',
        argv_encode(PopenStruct(
            fn,
            args,
            kwargs
        )),
    ]

    p = subprocess.Popen(args)
    return p


class PopenStack:
    """This is mainly for GC purposes. We wait instead of SIGKILL immediately."""

    def __init__(self, timeout=None):
        self.stack: List[subprocess.Popen] = []
        self.timeout = timeout

    def add(self, x: subprocess.Popen):
        self.stack.append(x)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.getLogger(__name__).debug('Exit %s %s %s', exc_type, exc_val, exc_tb)
        if exc_type:
            for x in self.stack:
                x.kill()
        else:
            try:
                for x in self.stack:
                    x.wait(timeout=self.timeout)
            except subprocess.TimeoutExpired:
                for x in self.stack:
                    x.send_signal(signal.SIGKILL)
                raise ValueError('Killed all of them!')


def popen_main():
    with ExitStack() as es:
        if os.environ.get('COVERAGE_PROCESS_START'):
            es.enter_context(cov())

        def popen_signal_handler(code, frame):
            if callable(prev_handler[code]):
                prev_handler[code](code, frame)

        codes = (signal.SIGINT, signal.SIGTERM)

        with signal_context(signals=codes, handler=popen_signal_handler) as prev_handlers:
            prev_handler = {k: v for k, v in zip(codes, prev_handlers)}

            try:
                defn: PopenStruct = argv_decode(sys.argv[2])
            except:
                import traceback
                import pprint

                fmtd = pprint.pformat(sys.argv)
                traceback.print_exc(file=sys.stderr)
                sys.stderr.flush()
                raise ValueError(f'Cannot unpickle arguments, called with {fmtd}')

            fn = defn.fn

            fn(*defn.args, **defn.kwargs)


if __name__ == '__main__':
    popen_main()
