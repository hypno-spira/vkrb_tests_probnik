from .base_page import BasePage
from .locators import AuthorizationPageLocators
from .locators import OnlineOrderPageLocators
from .locators import AdminCabinetAuthLocators
from .locators import AdminInvoicesPageLocators
import time
import re


class AdminInvoicesPage(BasePage):
    def sign_in(self, email, password):
        email_input = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.PASSWORD)
        password_input.send_keys(password)
        button_login = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.LOGIN_BUTTON)
        button_login.click()

    def new_order_should_be_in_first_line(self, new_order_id):
        order_id_in_first_line = (self.browser.find_element_by_css_selector(AdminInvoicesPageLocators.ORDER_ID_IN_THE_FIRST_LINE)).text
        assert new_order_id == int(order_id_in_first_line), f"в первой строке лежит другой заказ - {int(order_id_in_first_line)}, ожидался заказ {new_order_id}"

    def new_order_should_be_successful(self):
        status_in_the_first_line = (self.browser.find_element_by_css_selector(AdminInvoicesPageLocators.STATUS_IN_THE_FIRST_LINE)).text
        assert status_in_the_first_line == "completed", f"ожидался статус заказа completed, встречен - {status_in_the_first_line}"

    def new_order_should_be_unsuccessful(self):
        status_in_the_first_line = (
            self.browser.find_element_by_css_selector(AdminInvoicesPageLocators.STATUS_IN_THE_FIRST_LINE)).text
        assert status_in_the_first_line == "payment-error", f"ожидался статус заказа payment-error, встречен - {status_in_the_first_line}"

