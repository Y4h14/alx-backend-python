#!/usr/bin/env python3
"""define a sum_mixed_list function"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """sums ints and floats"""
    return sum(mxd_lst)
