import requests


def test_get_product_by_valid_id_returns_product_details():
    response = requests.get("https://dummyjson.com/products/1", timeout=5)

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 1
    assert isinstance(product["title"], str)
    assert product["title"]
    assert isinstance(product["category"], str)
    assert product["category"]
    assert isinstance(product["price"], (int, float))
    assert product["price"] >= 0
