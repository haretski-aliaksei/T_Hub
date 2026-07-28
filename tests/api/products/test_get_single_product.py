import pytest

from constants.api.products.fields import ERROR_MESSAGE
from constants.api.products.messages import product_not_found_message
from constants.api.products.test_data import PRODUCT_RESPONSE_DELAY_MS
from models.api.products.product import Product
from utils.api.products.test_data import (
    get_nonexistent_product_id,
    get_valid_product_id,
)


@pytest.mark.api
def test_get_product_by_valid_id(products_api):
    product_id = get_valid_product_id(products_api)

    response = products_api.get_product_by_id(product_id)

    assert response.status_code == 200

    product = Product.model_validate(response.json())

    assert product.id == product_id


@pytest.mark.api
def test_get_product_by_nonexistent_id(products_api):
    product_id = get_nonexistent_product_id(products_api)

    response = products_api.get_product_by_id(product_id)

    assert response.status_code == 404

    error = response.json()

    assert error[ERROR_MESSAGE] == product_not_found_message(product_id)


@pytest.mark.api
def test_get_product_by_valid_id_with_delay(products_api):
    product_id = get_valid_product_id(products_api)

    response = products_api.get_product_by_id(
        product_id,
        params={"delay": PRODUCT_RESPONSE_DELAY_MS},
    )

    assert response.status_code == 200

    product = Product.model_validate(response.json())

    assert product.id == product_id
