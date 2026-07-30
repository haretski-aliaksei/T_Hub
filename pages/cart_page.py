from pages.base_page import BasePage


class CartPage(BasePage):
    def start_checkout(self):
        self.page.locator('[data-test="checkout"]').click()

    def remove_backpack(self):
        self.page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    def get_cart_item_quantity(self):
        return self.page.locator('[data-test="item-quantity"]')

    def get_cart_item_name(self):
        return self.page.locator('[data-test="inventory-item-name"]')

    def get_cart_badge(self):
        return self.page.locator('[data-test="shopping-cart-badge"]')
