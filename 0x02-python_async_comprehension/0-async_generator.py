#!/usr/bin/env python3
"""defines a coroutine"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ a coroutine that yeild a random numbeir"""
    for i in range(10):
        yield random.uniform(0, 10)
