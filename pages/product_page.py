from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=20):
        super().__init__(browser, url, timeout)
        self.bookname = None
        self.bookprice = None

    def open(self):
        super().open()
        self.bookname = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CATALOG).text
        self.bookprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CATALOG).text
        print(self.bookname)
        print(self.bookprice)    
    
    def guest_add_product_to_basket(self):

        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_btn.click()
    
    
    def should_be_product_adding_success(self):
        add_feedback = self.browser.find_element(*ProductPageLocators.CART_FEEDBACK)
        item_class = add_feedback.get_attribute("className")
        assert "success" in item_class, "Add product to cart failed!"
        # assert item_class.find("success") != -1 , "Add product to cart failed!" 

    def should_be_cartproductname_equal_to_catalogproductname(self):
        product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART)
        text = product_name_el.text
        print(text)
        assert self.bookname == text, "Add product to cart failed. Bad name!"
        # assert text.find(self.bookname) != -1 ,  "Add product to cart failed. Bad name!"

    def should_be_cartproductprice_equal_to_catalogproductprice(self):    
        product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART)
        text = product_price_el.text
        print(text)
        assert self.bookprice in text, "Add product to cart failed. Bad price!"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MSG),\
            "Success message is presented"