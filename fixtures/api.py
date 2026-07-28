import pytest

from api.client import APIClient
from api.endpoints.products import ProductsAPI
from constants.api.urls import DUMMYJSON_BASE_URL


@pytest.fixture
def api_base_url():
    return DUMMYJSON_BASE_URL


@pytest.fixture
def api_client(api_base_url):
    return APIClient(api_base_url)


@pytest.fixture
def products_api(api_client):
    return ProductsAPI(api_client)
