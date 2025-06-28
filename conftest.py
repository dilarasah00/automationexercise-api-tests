import pytest
from config.endpoints import BASE_URL


@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

@pytest.fixture
def endpoint_factory(base_url):
    def make_endpoint(path):
        return f"{base_url}{path}"
    return make_endpoint