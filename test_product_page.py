import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time



@pytest.mark.user_add_product
class TestUserAddToBasketFromProductPage():    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser=browser, url=link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Qwert12#WEz"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        return browser

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"'    
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.should_not_be_success_message()


    # def test_user_can_add_product_to_basket(browser, link):
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.guest_add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_adding_success()
        product_page.should_be_cartproductname_equal_to_catalogproductname()
        product_page.should_be_cartproductprice_equal_to_catalogproductprice()
        # time.sleep(60)




# @pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.guest_go_to_basket()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()
    # time.sleep(10)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_link()
    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
# def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_adding_success()
    product_page.should_be_cartproductname_equal_to_catalogproductname()
    product_page.should_be_cartproductprice_equal_to_catalogproductprice()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'    
    product_page = ProductPage(browser=browser, url=link, timeout=0)
    product_page.open()
    product_page.guest_add_product_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'    
    product_page = ProductPage(browser=browser, url=link, timeout=0)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'    
    product_page = ProductPage(browser=browser, url=link, timeout=0)
    product_page.open()
    product_page.guest_add_product_to_basket()
    product_page.should_be_disappeared_success_message()





