import pytest
from playwright.sync_api import expect

from constants.ui.cart import (
    EXPECTED_CART_BADGE_FOR_ONE_ITEM,
    EXPECTED_CART_QUANTITY_FOR_ONE_ITEM,
)
from constants.ui.products import REMOVE_BUTTON_TEXT, SAUCE_LABS_BACKPACK
from constants.ui.urls import CART_PATH


@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.regression
def test_standard_user_can_add_product_to_cart(
    standard_user_session,
    products_page,
    cart_page,
):
    products_page.add_backpack_to_cart()

    expect(products_page.get_cart_badge()).to_have_text(
        EXPECTED_CART_BADGE_FOR_ONE_ITEM
    )
    expect(products_page.get_backpack_remove_button()).to_have_text(REMOVE_BUTTON_TEXT)

    products_page.open_cart()

    expect(cart_page.page).to_have_url(cart_page.get_url(CART_PATH))
    expect(cart_page.get_cart_item_quantity()).to_have_text(
        EXPECTED_CART_QUANTITY_FOR_ONE_ITEM
    )
    expect(cart_page.get_cart_item_name()).to_have_text(SAUCE_LABS_BACKPACK)
