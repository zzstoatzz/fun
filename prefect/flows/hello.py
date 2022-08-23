from operator import is_
from prefect import flow, get_run_logger, task
from typing import List


@task
def is_even(x: int) -> bool:
    return x % 2 == 0


@flow
def stoat():
    logger = get_run_logger()
    numbers = [i for i in range(10)]
    n_evens = sum(int(is_even(n)) for n in numbers)

    logger.info(f"There were {n_evens} in `numbers`")
