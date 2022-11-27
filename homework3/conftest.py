from api.client import ApiClient
import pytest


@pytest.fixture(scope='session')
def api_client():
    return ApiClient(base_url='https://target-sandbox.my.com/', login='povarov.vova99@gmail.com', password='Password!')
