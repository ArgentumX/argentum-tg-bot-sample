from functools import wraps
from typing import Callable

from events.event import Event

subscribes: dict[str, list[Callable]] = {}


def subscribe(event_class: type, handler: Callable[[Event], None]) -> None:
    event_name = event_class.__name__
    handlers = subscribes.get(event_name, [])
    initialized = bool(handlers)
    handlers.append(handler)
    if not initialized:
        subscribes[event_name] = handlers


async def call(event_instance) -> None:
    event_name = type(event_instance).__name__
    handlers = subscribes.get(event_name, [])
    for handler in handlers:
        await handler(event_instance)


class EventListener:
    def __init__(self, event_type: type):
        self._event_type = event_type

    def __call__(self, func):
        subscribe(self._event_type, func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
