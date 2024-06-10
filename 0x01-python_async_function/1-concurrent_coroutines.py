#!/usr/bin/env python3
"""defines an asynchronous function"""
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    """returns a list of random values"""
    delays = await asyncio.gather(*(wait_random(i) for i in range(n)))
    return delays
