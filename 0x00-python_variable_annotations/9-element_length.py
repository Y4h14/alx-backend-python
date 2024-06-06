#!/usr/bin/env python3
"""defines a length function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of Tuples"""
    return [(i, len(i)) for i in lst]
