from constants.api.products.fields import PRODUCT_ID, PRODUCTS, TOTAL
from constants.api.products.test_data import NONEXISTENT_PRODUCT_ID_OFFSET


def get_valid_product_id(products_api):
    response = products_api.get_products()

    assert response.status_code == 200

    products = response.json()[PRODUCTS]

    assert products

    for product in products:
        product_id = product.get(PRODUCT_ID)

        if isinstance(product_id, int):
            return product_id

    raise AssertionError("No product with valid id found")


def get_nonexistent_product_id(products_api):
    response = products_api.get_products()

    assert response.status_code == 200

    total = response.json()[TOTAL]

    assert isinstance(total, int)

    return total + NONEXISTENT_PRODUCT_ID_OFFSET
