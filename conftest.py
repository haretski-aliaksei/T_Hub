import pytest

from api.client import APIClient
from api.endpoints.products import ProductsAPI


@pytest.fixture
def base_url():
    return "https://dummyjson.com"


@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)


@pytest.fixture
def products_api(api_client):
    return ProductsAPI(api_client)
