import abc
import concurrent.futures
import threading
import typing
from . import _class_decorator

def cpu_count() -> int: ...

class APIPooled(_class_decorator.BaseDecorator, metaclass=abc.ABCMeta):
    @classmethod
    def configure(cls: typing.Type[APIPooled], max_workers: typing.Optional[int]=...) -> None: ...

    @classmethod
    def shutdown(cls: typing.Type[APIPooled]) -> None: ...

    @property
    def executor(self) -> typing.Any: ...

class BasePooled(APIPooled):
    @classmethod
    def configure(cls: typing.Type[BasePooled], max_workers: typing.Optional[int]=...) -> None: ...

    @classmethod
    def shutdown(cls: typing.Type[BasePooled]) -> None: ...

    @property
    def executor(self) -> ThreadPoolExecutor: ...

    def _get_function_wrapper(self, func: typing.Callable) -> typing.Callable[..., concurrent.futures.Future]: ...

class BaseThreaded(_class_decorator.BaseDecorator):
    def __init__(
        self,
        name: typing.Optional[typing.Union[str, typing.Callable]]=...,
        daemon: bool=...,
        started: bool=...
    ) -> None: ...

    @property
    def name(self) -> typing.Optional[str]: ...

    @property
    def daemon(self) -> bool: ...

    @property
    def started(self) -> bool: ...

    def _get_function_wrapper(self, func: typing.Callable) -> typing.Callable[..., threading.Thread]: ...

class ThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
    def __init__(self, max_workers: typing.Optional[int]=...) -> None: ...

    @property
    def max_workers(self) -> int: ...

    @property
    def is_shutdown(self) -> bool: ...
