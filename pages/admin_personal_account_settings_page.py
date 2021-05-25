from .base_page import BasePage
from .locators import AdminMonarchSettingsLocators
from selenium.webdriver.common.keys import Keys
import time


class AdminPersonalAccountSettingsPage(BasePage):
    def sign_in_admin_cabinet(self, email, password):  # вход в кабинет админа
        email_input = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.PASSWORD)
        password_input.send_keys(password)
        button_login = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.BUTTON_LOGIN)
        button_login.click()

    def select_login_validation_type__account_id(self):  # выбор login validation type как account id
        registration_tab = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.REGISTRATION_TAB)
        registration_tab.click()
        div = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.DIV)
        div.click()
        div_active = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.DIV_ACTIVE)
        div_active.send_keys(Keys.BACKSPACE)
        div_active.send_keys("Account ID" + Keys.ENTER)
        time.sleep(3)

    def save_changes_to_admin_cabinet(self):  # сохранить настройки
        button_save = self.browser.find_element_by_css_selector(AdminMonarchSettingsLocators.SAVE_BUTTON)
        button_save.click()
