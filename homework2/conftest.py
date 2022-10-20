from UI.fixtures import *
import os


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
