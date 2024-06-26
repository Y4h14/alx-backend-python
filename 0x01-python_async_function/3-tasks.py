#!/usr/bin/env python3
""" defines a function that takes an int and return a task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a new task """
    return asyncio.create_task(wait_random(max_delay))
