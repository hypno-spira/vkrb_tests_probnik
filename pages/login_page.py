from .base_page import BasePage
import time
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def sign_in_to_site(self, email, password, browser):  # заполнение верными данными
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        email_input = shadow_dom.find_element_by_css_selector("input#login.form-control")
        password_input = shadow_dom.find_element_by_css_selector("input#password.form-control")
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = shadow_dom.find_element_by_css_selector("button#buttonLogin.btn.btn-success.btn-block")
        button.click()
        time.sleep(3)

    def should_be_username_logo_in_the_header(self, browser):
        shadow_dom1 = self.expand_shadow_element(browser.find_element_by_tag_name("v-user-pop"))
        assert shadow_dom1.find_element_by_css_selector("span.span-name"), "В шапке нет имени пользователя - вход не выполнен"

    def should_be_message_about_wrong_password(self, browser):
        self.should_be_message_under_sign_in_button(browser)
        self.message_should_be_about_wrong_password(browser)

    def should_be_message_under_sign_in_button(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        assert shadow_dom.find_element_by_css_selector("div.alert.alert-danger"), "Сообщение не появилось"

    def message_should_be_about_wrong_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        message_text = (shadow_dom.find_element_by_css_selector("div.alert.alert-danger")).text
        assert message_text == "Wrong password", f"Появившееся сообщение - {message_text}"

    def register_on_the_site(self, sponsor_id, first_name, last_name, email, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        button_sign_up = shadow_dom.find_element_by_css_selector("#formLogin>div>h3>span.header-buttons>a")
        button_sign_up.click()
        time.sleep(3)
        sponsor_id_input = shadow_dom.find_element_by_css_selector("#lf-ref")
        first_name_input = shadow_dom.find_element_by_css_selector("#lf-4")
        last_name_input = shadow_dom.find_element_by_css_selector("#lf-5")
        email_input = shadow_dom.find_element_by_css_selector("#lf-6")
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        button_register = shadow_dom.find_element_by_css_selector("#buttonRegister")
        button_register.click()
        time.sleep(3)

    def should_be_message_about_wrong_sponsor_id(self, browser):
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_wrong_sponsor_id(browser)
        # дописать проверки

