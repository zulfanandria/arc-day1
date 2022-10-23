import pytest


def pytest_addoption(parser):
    parser.addoption("--name", action="store")


@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    return name_value
