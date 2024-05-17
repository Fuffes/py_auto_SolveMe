import random

import pytest


def _calculate(a, b):
    if isinstance(a,int) and isinstance(b, int):
        return a+b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_num():
    print("I am getting number")
    num = random.randrange(1, 100, 5)
    yield num
    print(f"nummm {num}")

