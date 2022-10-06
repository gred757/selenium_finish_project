from .locators import BasketPageLocators
from .main_page import MainPage

class BasketPage(MainPage):
    
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Product in basket found, but should not be!"
    
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Empty basket message not found!"
