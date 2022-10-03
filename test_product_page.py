import pytest

from pages.product_page import ProductPage
import time

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

    # try:
    #     product_page.should_be_product_adding_success()
    #     product_page.should_be_cartproductname_equal_to_catalogproductname()
    #     product_page.should_be_cartproductprice_equal_to_catalogproductprice()
    # except AssertionError as e:
    #     print("AssertionError: {}".format(e))
    #     print("Bugged link: {}".format(link))
    # finally:
    #     time.sleep(60)

