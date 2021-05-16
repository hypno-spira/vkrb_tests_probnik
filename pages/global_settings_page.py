from .base_page import BasePage
from selenium.webdriver.support.ui import Select


class GlobalSettingsPage(BasePage):
    def sign_in_configurator(self, email, password):
        email_input = self.browser.find_element_by_css_selector("#adminuserloginform-email")
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_css_selector("#adminuserloginform-password")
        password_input.send_keys(password)
        button_login = self.browser.find_element_by_css_selector("#login-form>div>div.button-pane>button")
        button_login.click()

    def select_login_type__id_as_login(self):
        select = Select(self.browser.find_element_by_css_selector("#globalsettingsform-login_type"))
        select.select_by_value("2")  # выбор элемента с текстом "ID As Login"

    def select_password_creation_type__by_user(self):
        select = Select(self.browser.find_element_by_css_selector("#globalsettingsform-password_creation_type"))
        select.select_by_value("1")  # выбор элемента с текстом "By User"

    def save_changes_to_global_settings(self):
        button_submit = self.browser.find_element_by_css_selector("#w0>div.panel-footer>div>div>button.btn.btn-success")
        button_submit.click()
