#!/usr/bin/env python3
"""define a function with a TypeVar"""
from typing import Any, Dict, Union, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """gets a value form a struct"""
    if key in dct:
        return dct[key]
    else:
        return default
