from .base_page import BasePage
from .locators import AdminCabinetAuthLocators
from selenium.webdriver.support.ui import Select


class GlobalSettingsPage(BasePage):
    def sign_in_configurator(self, email, password):
        email_input = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.PASSWORD)
        password_input.send_keys(password)
        button_login = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.LOGIN_BUTTON)
        button_login.click()

    def select_login_type__id_as_login(self):
        select = Select(self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.LOGIN_TYPE_SELECT))
        select.select_by_value("2")  # выбор элемента с текстом "ID As Login"

    def select_password_creation_type__by_user(self):
        select = Select(self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.PASS_CREATION_TYPE_SELECT))
        select.select_by_value("1")  # выбор элемента с текстом "By User"

    def save_changes_to_global_settings(self):
        button_submit = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.BUTTON_SUBMIT)
        button_submit.click()
