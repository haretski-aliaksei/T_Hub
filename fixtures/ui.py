import pytest

from constants.ui.urls import SAUCEDEMO_BASE_URL
from constants.ui.users import SAUCEDEMO_PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def ui_base_url():
    return SAUCEDEMO_BASE_URL


@pytest.fixture
def login_page(page, ui_base_url):
    return LoginPage(page, ui_base_url)


@pytest.fixture
def products_page(page, ui_base_url):
    return ProductsPage(page, ui_base_url)


@pytest.fixture
def cart_page(page, ui_base_url):
    return CartPage(page, ui_base_url)


@pytest.fixture
def checkout_page(page, ui_base_url):
    return CheckoutPage(page, ui_base_url)


@pytest.fixture
def standard_user_session(login_page):
    login_page.open()
    login_page.login(STANDARD_USER, SAUCEDEMO_PASSWORD)
