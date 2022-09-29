from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    # LOGIN_SUBMIT_BTN = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM  = (By.ID, "register_form")

    # LOGIN_FORM_USERNAME = (By.ID, "#id_login-username")
    # LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    # REGISTRATION_FORM_EMAIL = (By.ID, "#id_registration-email")
    # REGISTRATION_FORM_PASSWORD = (By.ID, "#id_registration-password1")
    # REGISTRATION_FORM_PASSWORD_CONFIRM = (By.ID, "#id_registration-password2")