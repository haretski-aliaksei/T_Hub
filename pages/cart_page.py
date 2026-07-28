from pages.base_page import BasePage


class CartPage(BasePage):
    def get_cart_item_quantity(self):
        return self.page.locator('[data-test="item-quantity"]')

    def get_cart_item_name(self):
        return self.page.locator('[data-test="inventory-item-name"]')
