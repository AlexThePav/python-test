import pytest
from .hooks import BaseTarget
from tests.test_scripts import test_something

def get_pytest_args():
    pytest_args = []
    pytest_args.append('-vs')
    pytest_args.append('./tests')
    return pytest_args

def main():
    my_plugin = BaseTarget()
    pytest.main(get_pytest_args(), plugins=[my_plugin])