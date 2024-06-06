#!/usr/bin/env python3
"""define a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a multiplier function"""
    def multiplier_jr(x: float) -> float:
        """multiply numbers"""
        return x * multiplier
    return multiplier_jr
