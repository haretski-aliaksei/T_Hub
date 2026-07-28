import pytest
from playwright.sync_api import expect

from constants.ui.messages import LOCKED_OUT_USER_ERROR
from constants.ui.urls import INVENTORY_PATH
from constants.ui.users import LOCKED_OUT_USER, SAUCEDEMO_PASSWORD, STANDARD_USER


@pytest.mark.ui
def test_standard_user_can_log_in(login_page):
    login_page.open()
    login_page.login(STANDARD_USER, SAUCEDEMO_PASSWORD)

    expect(login_page.page).to_have_url(login_page.get_url(INVENTORY_PATH))


@pytest.mark.ui
def test_locked_out_user_cannot_log_in(login_page):
    login_page.open()
    login_page.login(LOCKED_OUT_USER, SAUCEDEMO_PASSWORD)

    expect(login_page.get_error_message()).to_be_visible()
    expect(login_page.get_error_message()).to_contain_text(LOCKED_OUT_USER_ERROR)
