import pytest


@pytest.fixture(scope='class')
def time1():
    print('1')
    print('2')


@pytest.fixture(scope='test_01')
def time2():
    print('3')

