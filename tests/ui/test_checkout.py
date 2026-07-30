import pytest
from playwright.sync_api import expect

from constants.ui.checkout import (
    CHECKOUT_COMPLETE_MESSAGE,
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
)
from constants.ui.messages import CHECKOUT_FIRST_NAME_REQUIRED_ERROR
from constants.ui.products import SAUCE_LABS_BACKPACK
from constants.ui.urls import (
    CHECKOUT_COMPLETE_PATH,
    CHECKOUT_STEP_ONE_PATH,
    CHECKOUT_STEP_TWO_PATH,
)
from utils.ui.money import parse_currency


@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_can_complete_checkout(
    standard_user_session,
    products_page,
    cart_page,
    checkout_page,
):
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    expect(cart_page.get_cart_item_name()).to_have_text(SAUCE_LABS_BACKPACK)

    cart_page.start_checkout()

    expect(checkout_page.page).to_have_url(
        checkout_page.get_url(CHECKOUT_STEP_ONE_PATH)
    )

    checkout_page.fill_checkout_information(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE,
    )
    checkout_page.continue_checkout()

    expect(checkout_page.page).to_have_url(
        checkout_page.get_url(CHECKOUT_STEP_TWO_PATH)
    )

    checkout_page.finish_checkout()

    expect(checkout_page.page).to_have_url(
        checkout_page.get_url(CHECKOUT_COMPLETE_PATH)
    )
    expect(checkout_page.get_complete_header()).to_have_text(CHECKOUT_COMPLETE_MESSAGE)


@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.regression
def test_checkout_overview_total_equals_item_total_plus_tax(
    standard_user_session,
    products_page,
    cart_page,
    checkout_page,
):
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.start_checkout()

    checkout_page.fill_checkout_information(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE,
    )
    checkout_page.continue_checkout()

    item_total = parse_currency(checkout_page.get_item_total().text_content())
    tax = parse_currency(checkout_page.get_tax().text_content())
    total = parse_currency(checkout_page.get_total().text_content())

    assert total == round(item_total + tax, 2)


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.regression
def test_checkout_requires_first_name(
    standard_user_session,
    products_page,
    cart_page,
    checkout_page,
):
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.start_checkout()

    checkout_page.continue_checkout()

    expect(checkout_page.get_error_message()).to_be_visible()
    expect(checkout_page.get_error_message()).to_contain_text(
        CHECKOUT_FIRST_NAME_REQUIRED_ERROR
    )
