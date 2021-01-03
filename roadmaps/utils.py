from typing import Any, Callable, Collection

from toolz import curry


@curry
def extract(field: str, obj: object, default=None) -> Any:
    return getattr(obj, field, default)


extract_name = extract('name')
extract_data = extract('data')


@curry
def apply_tuple(func: Callable, args: Collection) -> Any:
    return func(*args)