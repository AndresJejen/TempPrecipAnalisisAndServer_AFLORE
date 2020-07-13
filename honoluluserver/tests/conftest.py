import pytest


from honoluluserver.app import create_app
from honoluluserver.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)