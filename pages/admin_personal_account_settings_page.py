from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class AdminPersonalAccountSettingsPage(BasePage):
    def sign_in_admin_cabinet(self, email, password):
        email_input = self.browser.find_element_by_css_selector(
            "#admin-login>form>div>div:nth-child(1)>div>div.form-data.block.size-2-3>div>input[type=text]")
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_css_selector(
            "#admin-login>form>div>div:nth-child(2)>div>div.form-data.block.size-2-3>div>input[type=password]")
        password_input.send_keys(password)
        button_login = self.browser.find_element_by_css_selector(
            "#admin-login>form>div>div.form-actions.primary-accent>button")
        button_login.click()

    def select_login_validation_type__account_id(self):
        registration_tab = self.browser.find_element_by_css_selector(
            "#blueprints > div > div > div.tabs-nav > a:nth-child(3)")
        registration_tab.click()
        div = self.browser.find_element_by_css_selector(
            "#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.full.has-options.has-items")
        div.click()
        div = self.browser.find_element_by_css_selector(
            "#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.has-options.full.has-items > input[type=select-one]")
        div.send_keys(Keys.BACKSPACE)
        div.send_keys("Account ID" + Keys.ENTER)
        time.sleep(3)

    def save_changes_to_admin_cabinet(self):
        button_save = self.browser.find_element_by_css_selector("#titlebar > div > button")
        button_save.click()

