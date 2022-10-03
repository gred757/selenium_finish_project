from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM  = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_FEEDBACK = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner")
    PRODUCT_NAME_CATALOG = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_CATALOG = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)  .alertinner > p strong")


    

     