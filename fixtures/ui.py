import pytest

from constants.ui.urls import SAUCEDEMO_BASE_URL
from pages.login_page import LoginPage


@pytest.fixture
def ui_base_url():
    return SAUCEDEMO_BASE_URL


@pytest.fixture
def login_page(page, ui_base_url):
    return LoginPage(page, ui_base_url)
