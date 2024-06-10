#!/usr/bin/env python3
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    delays = await asyncio.gather(*(wait_random(i) for i in range(n)))
    return delays