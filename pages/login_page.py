from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        super().open()

    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_error_message(self):
        return self.page.locator('[data-test="error"]')
