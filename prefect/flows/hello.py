from prefect import flow, get_run_logger, task
from random import randint
from typing import List

@task
def is_even(x: int) -> bool:
    return x % 2 == 0

@flow
def stoat(numbers: List[int] = [randint(0, 10) for i in range(10)]):
    logger = get_run_logger()
    logger.info(sum(int(is_even(n) for n in numbers)))