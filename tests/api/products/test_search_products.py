import pytest

from constants.api.products.fields import PRODUCTS, TOTAL
from constants.api.products.test_data import NO_MATCH_SEARCH_QUERY


@pytest.mark.api
@pytest.mark.regression
def test_search_products_with_no_matches_returns_empty_response(products_api):
    response = products_api.search_products(NO_MATCH_SEARCH_QUERY)

    assert response.status_code == 200

    body = response.json()

    assert body[PRODUCTS] == []
    assert body[TOTAL] == 0
