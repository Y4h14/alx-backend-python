#!/usr/bin/env python3
""" defines a function"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return the first element of a sequence or none"""
    if lst:
        return lst[0]
    else:
        return None
