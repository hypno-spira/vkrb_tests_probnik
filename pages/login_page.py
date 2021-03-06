from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .links import Links
from .locators import CabinetLocators
from .locators import AuthorizationPageLocators
from .locators import DashboardPageLocators
from .locators import RegistrationPageLocators
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def sign_in_to_site(self, email, password, browser):  # авторизация
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        email_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_EMAIL)
        password_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_BUTTON)
        button.click()
        time.sleep(2)

    # def should_be_username_logo_in_the_header(self, browser):  # отображение имени Lesa Miller в шапке
    #     shadow_dom1 = self.expand_shadow_element(browser.find_element_by_tag_name(DashboardPageLocators.SHADOW_TAG))
    #     browser.implicitly_wait(10)
    #     self.dashboard_should_be_open()
    #     username = (shadow_dom1.find_element_by_css_selector(DashboardPageLocators.USERNAME_ON_HEADER)).text
    #     assert username == "Lesa Miller", f"В шапке либо отсутствует, либо другое имя пользователя - {username} "

    def should_be_message_about_wrong_password(self, browser):  # появление сообщения - неверный пароль
        self.should_be_message_under_sign_in_button(browser)
        self.message_should_be_about_wrong_password(browser)

    def should_be_message_under_sign_in_button(self, browser):  # появление сообщения
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.ALERT_DANGER), "Сообщение не появилось"

    def message_should_be_about_wrong_password(self, browser):  # сообщение о неверном пароле
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.ALERT_DANGER)).text
        assert message_text == "Wrong password", f"Появившееся сообщение - {message_text}"

    def register_on_the_site(self, sponsor_id, first_name, last_name, email, browser):  # регистрация
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        button_sign_up = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.SIGN_UP_BUTTON)
        button_sign_up.click()
        time.sleep(2)
        sponsor_id_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.SPONSOR_ID)
        first_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.FIRST_NAME)
        last_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.LAST_NAME)
        email_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.EMAIL)
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        button_register = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.REGISTER_BUTTON)
        button_register.click()
        time.sleep(2)

    def should_be_message_about_wrong_sponsor_id(self, browser, sponsor_id):  # поиск сообщения о неверном sponsor id
        time.sleep(2)
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_wrong_sponsor_id(browser, sponsor_id)

    def should_be_message_in_the_lower_right_corner(self, browser):  # поиск сообщения
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE), "Сообщение в правом нижнем углу не появилось"

    def message_should_be_about_wrong_sponsor_id(self, browser, sponsor_id):  # сообщение должно быть о неверном sponsor id
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE_TEXT)).text
        assert message_text == f"Sponsor account with Id '{sponsor_id}' not exists", f"Появившееся сообщение - {message_text}"

    def should_be_message_email_already_exists(self, browser):  # поиск сообщения об уже сущ. email
        time.sleep(2)
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_email_already_exists(browser)

    def message_should_be_about_email_already_exists(self, browser):  # сообщение должно быть об уже сущ. email
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE_TEXT)).text
        assert message_text == "Can not user create." or message_text == "User already exists", f"Появившееся сообщение - {message_text}"

    def should_be_message_about_registration_confirmation_via_email(self, browser):  # поиск сообщения об успешной регистрации
        time.sleep(2)
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (
            shadow_dom.find_element_by_css_selector(RegistrationPageLocators.CONFIRM_MESSAGE)).text
        assert message_text == "User created", "Регистрация не была пройдена"

    def email_field_is_not_present(self, browser, timeout=3):  #
        try:
            shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
            email_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.EMAIL)
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(email_input))
        except TimeoutException:
            return True
        return False

    def should_be_added_fields_password_and_confirm_password(self, browser):  # должны добавиться 2 поля password
        time.sleep(2)
        self.delete_cache(browser)
        online_order_page = LoginPage(browser, Links.AUTH_RU)
        online_order_page.open()
        time.sleep(2)
        online_order_page = LoginPage(browser, Links.DASHBOARD_LINK) # смена языка туда и обратно
        online_order_page.open()
        time.sleep(2)
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        button_sign_up = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.SIGN_UP_BUTTON)
        button_sign_up.click()
        self.should_be_added_field_password(browser)
        self.should_be_added_field_confirm_password(browser)

    def delete_cache(self, browser):
        browser.execute_script("window.open('');")
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[-1])
        time.sleep(2)
        browser.get('chrome://settings/clearBrowserData')  # for old chromedriver versions use cleardriverData
        time.sleep(2)
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
        actions.perform()
        time.sleep(2)
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
        actions.perform()
        time.sleep(5)  # wait some time to finish
        browser.close()  # close this tab
        browser.switch_to.window(browser.window_handles[0])  # switch back

    def should_be_added_field_password(self, browser):  # должно добавиться поле password
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1), "Поле password1 не появилось"

    def should_be_added_field_confirm_password(self, browser):  # должно добавиться поле  confirm password
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1), "Поле password2 не появилось"

    def success_registration(self, sponsor_id, first_name, last_name, password, browser):  # регистрация после изменения полей
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        sponsor_id_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.SPONSOR_ID)
        first_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.FIRST_NAME)
        last_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.LAST_NAME)
        password_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1)
        password2_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_2)
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        password_input.send_keys(password)
        password2_input.send_keys(password)
        button_register = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.REGISTER_BUTTON)
        button_register.click()
        time.sleep(3)

    def dashboard_should_be_open(self, browser):  # должен открыться Dashboard
        time.sleep(7)
        dashboard_label = self.browser.find_element_by_css_selector(DashboardPageLocators.DASHBOARD_LABEL)
        assert dashboard_label.text == "DASHBOARD", \
            f"заголовок h2 не найден или найден с текстом {dashboard_label.text}"
