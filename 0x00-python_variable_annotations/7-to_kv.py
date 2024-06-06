#!/usr/bin/env python3
"""define a to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a Tuple"""
    return (k, v**2)
