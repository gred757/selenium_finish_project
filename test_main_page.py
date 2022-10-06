import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser=browser, url=link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser=browser, url=link)
    main_page.open()
    main_page.guest_go_to_cart()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.open()
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.should_be_login_page()

