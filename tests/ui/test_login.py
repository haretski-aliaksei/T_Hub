import pytest
from playwright.sync_api import expect

from constants.ui.urls import INVENTORY_PATH
from constants.ui.users import SAUCEDEMO_PASSWORD, STANDARD_USER


@pytest.mark.ui
def test_standard_user_can_log_in(login_page):
    login_page.open()
    login_page.login(STANDARD_USER, SAUCEDEMO_PASSWORD)

    expect(login_page.page).to_have_url(login_page.get_url(INVENTORY_PATH))
