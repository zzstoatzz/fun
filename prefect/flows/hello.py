from prefect import flow, task
from typing import List


@task
def is_even(x: int) -> bool:
    return x % 2 == 0


@flow
def stoat(numbers: List[int]):
    print(numbers)
