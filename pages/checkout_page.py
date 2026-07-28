from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').fill(postal_code)

    def continue_checkout(self):
        self.page.locator('[data-test="continue"]').click()

    def finish_checkout(self):
        self.page.locator('[data-test="finish"]').click()

    def get_complete_header(self):
        return self.page.locator('[data-test="complete-header"]')
