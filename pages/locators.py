from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(BasePageLocators):
    BASKET_BUTTON = (By.XPATH, "//*[contains(@class,'basket-mini')]//a[contains(@class, 'btn-default') and contains(@href, 'basket')]")
    

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM  = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    SUBMIT_REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(MainPageLocators):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_FEEDBACK = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner")
    PRODUCT_NAME_CATALOG = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_CATALOG = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)  .alertinner > p strong")
    