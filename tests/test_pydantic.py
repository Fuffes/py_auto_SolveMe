import pytest
from src.generators.local_gen import LocalGen
from src.pydantic_schemas.computer import Computer
from


def test_some1():
    """test pydantic schema"""
    comp = Computer.parse_obj()
