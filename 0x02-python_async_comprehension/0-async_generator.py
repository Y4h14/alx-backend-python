#!/usr/bin/env python3
"""defines a coroutine"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """ a coroutine that yeild a random numbeir"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
