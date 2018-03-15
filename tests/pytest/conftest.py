import pytest


@pytest.fixture(scope='module')
def wrap():
    print('set up')
    yield
    print('tear down')
