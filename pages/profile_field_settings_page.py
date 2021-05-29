from .base_page import BasePage
from .locators import AdminCabinetAuthLocators
import time


class ProfileFieldSettingsPage(BasePage):
    def uncheck_email_field(self):  # снять чек-бокс email
        email_checkbox = self.browser.find_element_by_css_selector(AdminCabinetAuthLocators.EMAIL_CHECKBOX)
        email_checkbox.click()
        time.sleep(5)

