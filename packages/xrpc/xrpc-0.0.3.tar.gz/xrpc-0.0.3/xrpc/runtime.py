import logging
import threading
from typing import Optional, NamedTuple, Callable, Dict, TypeVar, Type, Any

from xrpc.client import ClientConfig, ServiceWrapper
from xrpc.net import RPCKey
from xrpc.service import ServiceDefn
from xrpc.transport import Origin, RPCTransportStack

RUNTIME_TL = threading.local()
CTX_NAME = 'rpc_config'
CACHE_NAME = 'rpc_cache'


class ExecutionContext(NamedTuple):
    transport_stack: RPCTransportStack
    origin: Optional[Origin] = None
    key: Optional[RPCKey] = None
    ret: Optional[Callable[[Any], None]] = None

    def exec(self, __origin, __fn: Callable, *args, **kwargs):
        is_ok = False
        r = None

        logging.getLogger(f'xrpc.trace.e.{__origin}').debug('Name=%s %s %s %s %s', __fn.__name__, is_ok, args, kwargs, r)
        try:
            context_set(self)

            r = __fn(*args, **kwargs)
            is_ok = True
            return r
        finally:
            logging.getLogger(f'xrpc.trace.x.{__origin}').debug('Name=%s %s %s %s %s', __fn.__name__, is_ok, args, kwargs, r)
            context_set(None)


def context_set(config: Optional[ExecutionContext]):
    if sender:
        setattr(RUNTIME_TL, CTX_NAME, config)
    elif hasattr(RUNTIME_TL, CTX_NAME):
        delattr(RUNTIME_TL, CTX_NAME)


def cache_get() -> Dict[Type, ServiceDefn]:
    if not hasattr(RUNTIME_TL, CACHE_NAME):
        nd = {}
        setattr(RUNTIME_TL, CACHE_NAME, nd)

    return getattr(RUNTIME_TL, CACHE_NAME)


def context() -> ExecutionContext:
    return getattr(RUNTIME_TL, CTX_NAME)


def sender() -> Origin:
    return context().origin


def reply(ret: Any):
    ctx = context()

    ctx.ret(ret)


T = TypeVar('T')


def service(obj: Type[T], addr: Origin, conf: ClientConfig = ClientConfig()) -> T:
    ctx = context()

    service_cache = cache_get()

    if obj in service_cache:
        defn = service_cache[obj]
    else:
        defn = ServiceDefn.from_obj(obj)
        service_cache[obj] = defn

    return ServiceWrapper(defn, conf, ctx.transport_stack, addr)
