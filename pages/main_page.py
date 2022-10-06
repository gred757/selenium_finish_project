from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def guest_go_to_cart(self):
        cart_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        cart_button.click()
