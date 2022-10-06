from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_el = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_el.send_keys(email)
        password_el = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_el.send_keys(password)
        password_confirm_el = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_confirm_el.send_keys(password)
        submit_btn_el = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER_BUTTON)
        submit_btn_el.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") > -1, "Login url is missing" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found!"







