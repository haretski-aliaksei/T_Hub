import pytest


@pytest.mark.api
def test_get_product_by_valid_id_returns_product_details(products_api):
    response = products_api.get_product_by_id(1)

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 1
    assert isinstance(product["title"], str)
    assert product["title"]
    assert isinstance(product["category"], str)
    assert product["category"]
    assert isinstance(product["price"], (int, float))
    assert product["price"] >= 0
