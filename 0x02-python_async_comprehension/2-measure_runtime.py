#!/usr/bin/env python3
""" define a runtime measure function """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    runs aysnc_comperhension coroutine 4 times
    in parrellel using asyncio.gather and retuns
    the run time
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time.time() - start_time
