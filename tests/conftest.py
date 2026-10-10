import pytest
from utils.request_util import RequestsUtil

@pytest.fixture(scope = "session")
def json_api():
    client = RequestsUtil(base_url="https://jsonplaceholder.typicode.com")
    yield client
    client.close()

@pytest.fixture(scope = "session")
def httpbin_api():
    client = RequestsUtil(base_url="https://httpbin.org")
    yield client
    client.close()

