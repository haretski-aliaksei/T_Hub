from pages.base_page import BasePage


class ProductsPage(BasePage):
    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def get_backpack_remove_button(self):
        return self.page.locator('[data-test="remove-sauce-labs-backpack"]')

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def get_cart_badge(self):
        return self.page.locator('[data-test="shopping-cart-badge"]')
