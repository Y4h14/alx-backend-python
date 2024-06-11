#!/usr/bin/env python3
"""defines a coroutine"""
import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers using async comprehention"""
    return [number async for number in async_generator()]
