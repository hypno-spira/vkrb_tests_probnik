from .base_page import BasePage



class ProfileFieldSettingsPage(BasePage):
    def uncheck_email_field(self):
        email_checkbox = self.browser.find_element_by_css_selector("#profileFieldsGrid-container>table>tbody>tr:nth"
                                                                   "-child(3)>td:nth-child(4)>input[type=checkbox]")
        email_checkbox.click()

